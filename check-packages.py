#!/usr/bin/env python3

import subprocess
from optparse import OptionParser
from stat import *
import sys
import os
import atexit

RECIPE_DEPNDS_FILE = "./recipe-depends.dot"

def remove_packages_in_whitelist(packages, whitelist):
    result = {}
    
    for pkgname in packages:
        if not pkgname in whitelist:
            result[pkgname] = packages[pkgname]
    return result

def remove_packages_not_in_manifest(packages, target_packages):
    result = {}
    
    for pkgname in packages:
        if pkgname in target_packages:
            result[pkgname] = packages[pkgname]
    
    return result
    
def read_whitelist(whitelist_file):
    whitelist = []
    
    with open(whitelist_file, "r") as f:
        for line in f.readlines():
            if not line.startswith("#"):
                whitelist.append(line.strip())

    return whitelist

def run_cmd(cmd):
    lines = []
    
    with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
        proc.wait()
        retcode = proc.returncode

        for line in proc.stdout.readlines():
            lines.append(line.decode('utf-8'))

        return {
            "returncode": int(retcode),
            "lines": lines
        }
    return None

def create_dependencies_files(target, sdkflag):
    # bitbake -g core-image-minimal -c populate_sdk

    cmd = [ "bitbake", "-g", target ]
    if sdkflag:
        cmd = cmd + [ "-c", "populate_sdk" ]

    result =run_cmd(cmd)

    return os.path.exists(RECIPE_DEPNDS_FILE)

def parse_info_line(line):
    arr = line.split(' ')

    pkgname = arr[0].replace('"', '').strip()
    
    tmp = arr[1].strip().split('\\n')
    path = tmp[-1]
    
    if ":" in path:
        path = path.split(":")[-1]
        
    path = path.replace(']', '').replace('"', '')
        
    version = tmp[1].strip(':')
        
    return {
        "pkgname": pkgname,
        "bbpath": path,
        "version": version,
    }
        
def read_dependencies_dot_file():
    data = {}
    
    with open(RECIPE_DEPNDS_FILE, "r") as f:
        lines = f.readlines()

        for line in lines:
            if "label=" in line:
                d = parse_info_line(line)
                name = d["pkgname"]
                data[name] = d
                
    return data

def set_layer_info(pkglist, layers):

    for name in pkglist:
        pkg = pkglist[name]

        for layer in layers:
            layer_path = layers[layer]["path"]
            
            if pkg["bbpath"].startswith(layer_path):
                pkg["layer"] = layer
        
def find_packages_not_built_from_debian(packages, base_workdir):
    cmd = ["find", base_workdir, "-maxdepth", "2", "-type", "d"]
    
    result = run_cmd(cmd)

    package_dirs = result["lines"]
    result = {}
    
    for package_dir in package_dirs:
        
        package_dir = package_dir.strip()
        pkgname = os.path.basename(package_dir)

        if pkgname in packages.keys():
            cmd = ["find", package_dir, "-maxdepth", "2", "-name", "*.dsc"]
            dsc_result = run_cmd(cmd)
            
            if len(dsc_result["lines"]) is 0:
                result[pkgname] = packages[pkgname]
                
    return result
                
def get_bitbake_envs():
    cmd = ["bitbake", "-e"]
    lines = []

    result = {}

    with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
        for line in proc.stdout.readlines():
            l = line.decode('utf-8')
    
            if l.startswith("BASE_WORKDIR=") or \
               l.startswith("TMPDIR="):
                tmp  = l.strip().replace('"', '').split('=')
                result[tmp[0]] = tmp[1]

    if len(result) is 0:
        print("Cannot get BASE_WORKDIR environment", file=sys.stderr)
        exit(1)

    return result

def has_bitbake():
    cmd = ["which", "bitbake-layers"]
    result = run_cmd(cmd)
    if not result["returncode"] == 0:
        print("[*] bitbake-layers command isn't in your $PATH")
        exit(-1)

def get_layers():
    cmd = ["bitbake-layers", "show-layers"]

    layers = {}
    
    result = run_cmd(cmd)
    lines = result["lines"]

    # remove header lines
    for i in range(3):
        lines.pop(0)
        
    for line in lines:
        tmp = line.strip().split()
        layer_path = tmp[1]
        if not layer_path.endswith("/"):
            layer_path = "%s/" % layer_path
        layer = {
            "name": tmp[0],
            "path": layer_path,
            "prio": int(tmp[2])
        }

        layers[layer["name"]] = layer

    return layers

def get_packages_from_manifest(manifestfile):
    packages = []

    with open(manifestfile, "r") as f:
        lines = f.readlines()

        for line in lines:
            packages.append(line.split(' ')[0].strip())

    return packages


def show_no_data():
    print("All packages are built from debian source!")

def print_data(pkgname, layer, version, bbpath):
    print("%s\t%s\t%s\t%s" % (pkgname.ljust(60), layer.ljust(20), version.ljust(30), bbpath.ljust(120)))
    
def show_result(data):
    if len(data) == 0:
        show_no_data()
        return 0
    
    print("==== Packages not built from debian source ====")

    print_data("package name", "layer", "version", "bbfile path")
    for k in data.keys():
        d = data[k]
        print_data(d["pkgname"], d["layer"], d["version"], d["bbpath"])

    return 1

def parse_arguments():
    usage = "usage: %prog [options] WHITELIST target"
    
    parser = OptionParser(usage=usage)

    parser.add_option("-s", "--sdk", dest="sdkflag",
                      help="check sdk", action="store_true", default=False)

    parser.add_option("-m", "--manifest", dest="manifest",
                       help="path to manifestfile for image, target sdk, host sdk(e.g. $BASE_WORKDIR/tmp/deploy/images/qemuarm64/core-image-minimal-qemuarm64.manifest, $BASE_WORKDIR/tmp/deploy/sdk/emlinux-glibc-x86_64-core-image-minimal-aarch64-toolchain-2.0.target.manifest)",
                       metavar="MANIFEST", default=None)

    (options, args) = parser.parse_args()

    if not len(args) == 2:
        print("must specify whitelist and target", file=sys.stderr)
        print("target is bitbake target such as core-image-minimal")
        exit(1)

    return {
        "sdkflag": options.sdkflag,        
        "manifest": options.manifest,
        "whitelist": args[0],
        "target": args[1],
    }

def sort_package_data(packages):
    sorted_packages = {}
    for k, v in sorted(packages.items(), key=lambda x: x[0]):
        sorted_packages[k] = v

    return sorted_packages

def cleanup_all():
    dot_files = [ RECIPE_DEPNDS_FILE, "./pn-buildlist", "./task-depends.dot"]

    for f in dot_files:
        if os.path.exists(f):
            os.unlink(f)
            
if __name__ == "__main__":
    atexit.register(cleanup_all)
    
    args = parse_arguments()

    whitelist = read_whitelist(args["whitelist"])
    
    has_bitbake()

    bitbake_envs = get_bitbake_envs()
    
    layers = get_layers()
    
    packages = None

    if not create_dependencies_files(args["target"], args["sdkflag"]):
        print("failed to create %s file" % RECIPE_DEPNDS_FILE, file=sys.stderr)
        exit(1)
    
    pkglist = read_dependencies_dot_file()

    set_layer_info(pkglist, layers)
    
    if not args["manifest"]:
        packages = pkglist
    else:
        target_packages = get_packages_from_manifest(args["manifest"])
        packages = remove_packages_not_in_manifest(pkglist, target_packages)

    packages = find_packages_not_built_from_debian(packages, bitbake_envs["BASE_WORKDIR"])

    # remove package that is in whitelist
    packages = remove_packages_in_whitelist(packages, whitelist)

    r = show_result(sort_package_data(packages))
    
    exit(r)
