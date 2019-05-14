# Check packge is build from debian source

The check-package.py checks that package is built from debian source or not.

## whitelist 

Some packages don't have to be built from debian so they are listed in whitelist/recipes-whitelist.txt. This list is based on [this status pabe](https://iwamatsu.github.io/meta-debian-extended/) that status is _ignore_ .

Whitelist file is plain text file. This file is able to write comment starts with _#_.

## how to use

This program takes least two parameters. 
1. whitelist
2. target

The whitelist is a list file that contains recipe names that allows package build from debian source.
The target option is same as target option to bitbake such as core-image-minimal.

### exit code

0 means all packages are built from debian source. 1 means some of package(s) is built from not debian source.

### check all package

e.g.

```
$ ./check-packages.py whitelist/recipes-whitelist.txt core-image-minimal
==== Packages not built from debian source ====
package name                                                    layer                   version                         bbfile path
apt-native                                                      meta                    1.2.24-r0                       /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/apt/apt-native_1.2.24.bb
autoconf-native                                                 meta                    2.69-r11                        /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/autoconf/autoconf_2.69.bb
automake-native                                                 meta                    1.16.1-r0                       /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/automake/automake_1.16.1.bb
cross-localedef-native                                          meta                    2.29-r0                         /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-core/glibc/cross-localedef-native_2.29.bb
cwautomacros-native                                             meta                    20110201-r0                     /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-extended/cwautomacros/cwautomacros_20110201.bb
dwarfsrcfiles-native                                            meta                    1.0-r0                          /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/dwarfsrcfiles/dwarfsrcfiles.bb
gcc-cross-aarch64                                               meta-debian             8.3.0-r0                        /home/masami/projects/emlinux/emlinux/repos/meta-debian/recipes-debian/gcc/gcc-cross_debian.bb
gcc-cross-canadian-aarch64                                      meta-debian             8.3.0-r0                        /home/masami/projects/emlinux/emlinux/repos/meta-debian/recipes-debian/gcc/gcc-cross-canadian_debian.bb
gcc-crosssdk-x86_64-emlinuxsdk-linux                            meta-debian             8.3.0-r0                        /home/masami/projects/emlinux/emlinux/repos/meta-debian/recipes-debian/gcc/gcc-crosssdk_debian.bb
gettext-minimal-native                                          meta                    0.19.8.1-r0                     /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-core/gettext/gettext-minimal-native_0.19.8.1.bb
gettext-native                                                  meta                    0.19.8.1-r0                     /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-core/gettext/gettext_0.19.8.1.bb
glibc-locale                                                    meta-debian             2.29-r0                         /home/masami/projects/emlinux/emlinux/repos/meta-debian/recipes-debian/glibc/glibc-locale_debian.bb
gnu-config-native                                               meta                    20181128+gitAUTOINC+058639be22-r0       /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/gnu-config/gnu-config_git.bb
kern-tools-native                                               meta                    0.2+gitAUTOINC+af1a779f66-r12   /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-kernel/kern-tools/kern-tools-native_git.bb
ldconfig-native                                                 meta                    2.12.1-r2                       /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-core/glibc/ldconfig-native_2.12.1.bb
libgcc                                                          meta-debian             8.3.0-r0                        /home/masami/projects/emlinux/emlinux/repos/meta-debian/recipes-debian/gcc/libgcc_debian.bb
libgcc-initial                                                  meta-debian             8.3.0-r0                        /home/masami/projects/emlinux/emlinux/repos/meta-debian/recipes-debian/gcc/libgcc-initial_debian.bb
libnsl2-native                                                  meta                    1.2.0+gitAUTOINC+37c5ffe303-r0  /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-extended/libnsl/libnsl2_git.bb
libtool-native                                                  meta                    2.4.6-r0                        /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/libtool/libtool-native_2.4.6.bb
m4-native                                                       meta                    1.4.18-r0                       /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/m4/m4-native_1.4.18.bb
makedevs-native                                                 meta                    1.0.1-r0                        /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/makedevs/makedevs_1.0.1.bb
meta-environment-qemuarm64                                      meta                    1.0-r8                          /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-core/meta/meta-environment.bb
nativesdk-gcc-runtime                                           meta-debian             8.3.0-r0                        /home/masami/projects/emlinux/emlinux/repos/meta-debian/recipes-debian/gcc/gcc-runtime_debian.bb
nativesdk-glibc-locale                                          meta-debian             2.29-r0                         /home/masami/projects/emlinux/emlinux/repos/meta-debian/recipes-debian/glibc/glibc-locale_debian.bb
nativesdk-gnu-config                                            meta                    20181128+gitAUTOINC+058639be22-r0       /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/gnu-config/gnu-config_git.bb
nativesdk-libgcc                                                meta-debian             8.3.0-r0                        /home/masami/projects/emlinux/emlinux/repos/meta-debian/recipes-debian/gcc/libgcc_debian.bb
nativesdk-libgcc-initial                                        meta-debian             8.3.0-r0                        /home/masami/projects/emlinux/emlinux/repos/meta-debian/recipes-debian/gcc/libgcc-initial_debian.bb
nativesdk-libnsl2                                               meta                    1.2.0+gitAUTOINC+37c5ffe303-r0  /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-extended/libnsl/libnsl2_git.bb
nativesdk-libsolv                                               meta                    0.7.3-r0                        /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-extended/libsolv/libsolv_0.7.3.bb
nativesdk-linux-libc-headers-base                               meta-debian             gitAUTOINC+e2a020d7b8-r0        /home/masami/projects/emlinux/emlinux/repos/meta-debian/recipes-kernel/linux-libc-headers/linux-libc-headers-base_git.bb
nativesdk-makedevs                                              meta                    1.0.1-r0                        /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/makedevs/makedevs_1.0.1.bb
nativesdk-meson                                                 meta                    0.49.2-r0                       /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/meson/nativesdk-meson_0.49.2.bb
nativesdk-opkg                                                  meta                    1:0.4.0-r0                      /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/opkg/opkg_0.4.0.bb
nativesdk-opkg-utils                                            meta                    0.4.0-r0                        /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/opkg-utils/opkg-utils_0.4.0.bb
nativesdk-packagegroup-sdk-host                                 meta                    1.0-r12                         /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-core/packagegroups/nativesdk-packagegroup-sdk-host.bb
nativesdk-python3                                               meta                    3.7.2-r0                        /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/python/python3_3.7.2.bb
nativesdk-python3-setuptools                                    meta                    40.8.0-r0                       /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/python/python3-setuptools_40.8.0.bb
nativesdk-qemu                                                  meta                    3.1.0-r0                        /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/qemu/qemu_3.1.0.bb
nativesdk-qemu-helper                                           meta                    1.0-r9                          /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/qemu/nativesdk-qemu-helper_1.0.bb
nativesdk-qemuwrapper-cross                                     meta                    1.0-r0                          /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/qemu/qemuwrapper-cross_1.0.bb
nativesdk-sdk-provides-dummy                                    meta                    1.0-r0                          /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-core/meta/nativesdk-sdk-provides-dummy.bb
nativesdk-sqlite3                                               meta                    3:3.27.2-r0                     /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-support/sqlite/sqlite3_3.27.2.bb
nativesdk-unfs3                                                 meta                    0.9.22.r497-r0                  /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/unfs3/unfs3_0.9.22.r497.bb
nativesdk-util-macros                                           meta                    1:1.19.2-r0                     /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-graphics/xorg-util/util-macros_1.19.2.bb
nativesdk-xz                                                    meta                    5.2.4-r0                        /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-extended/xz/xz_5.2.4.bb
opkg-utils-native                                               meta                    0.4.0-r0                        /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/opkg-utils/opkg-utils_0.4.0.bb
packagegroup-core-standalone-sdk-target                         meta                    1.0-r8                          /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-core/packagegroups/packagegroup-core-standalone-sdk-target.bb
packagegroup-cross-canadian-qemuarm64                           meta                    1.0-r0                          /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-core/packagegroups/packagegroup-cross-canadian.bb
prelink-native                                                  meta                    1.0+gitAUTOINC+a853a5d715-r0    /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/prelink/prelink_git.bb
python3                                                         meta                    3.7.2-r0                        /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/python/python3_3.7.2.bb
python3-native                                                  meta                    3.7.2-r0                        /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/python/python3_3.7.2.bb
python3-setuptools-native                                       meta                    40.8.0-r0                       /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/python/python3-setuptools_40.8.0.bb
qemu-native                                                     meta                    3.1.0-r0                        /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/qemu/qemu-native_3.1.0.bb
quilt-native                                                    meta                    0.65-r0                         /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/quilt/quilt-native_0.65.bb
sqlite3                                                         meta                    3:3.27.2-r0                     /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-support/sqlite/sqlite3_3.27.2.bb
sqlite3-native                                                  meta                    3:3.27.2-r0                     /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-support/sqlite/sqlite3_3.27.2.bb
target-sdk-provides-dummy                                       meta                    1.0-r0                          /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-core/meta/target-sdk-provides-dummy.bb
texinfo-dummy-native                                            meta                    1.0-r0                          /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-extended/texinfo-dummy-native/texinfo-dummy-native.bb
tzcode-native                                                   meta                    2019a-r0                        /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-extended/timezone/tzcode-native.bb
update-rc.d-native                                              meta                    0.8-r0                          /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-core/update-rc.d/update-rc.d_0.8.bb
util-macros-native                                              meta                    1:1.19.2-r0                     /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-graphics/xorg-util/util-macros_1.19.2.bb
xz                                                              meta                    5.2.4-r0                        /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-extended/xz/xz_5.2.4.bb
xz-native                                                       meta                    5.2.4-r0                        /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-extended/xz/xz_5.2.4.bb
```

### check packages in core-image-minimal

e.g.

```
$ ./check-packages.py whitelist/recipes-whitelist.txt core-image-minimal -s -m ../emlinux/build/tmp-glibc/deploy/images/qemuarm64/core-image-minimal-qemuarm64.manifest
All packages are built from debian source!
```

### check host sdk

Check host target sdk.

```
$ ./check-packages.py whitelist/recipes-whitelist.txt core-image-minimal -s -m ../emlinux/build/tmp-glibc/deploy/sdk/emlinux-glibc-x86_64-core-image-minimal-aarch64-toolchain-2.0.host.manifest
==== Packages not built from debian source ====
package name                                                    layer                   version                         bbfile path
gcc-cross-canadian-aarch64                                      meta-debian             8.3.0-r0                        /home/masami/projects/emlinux/emlinux/repos/meta-debian/recipes-debian/gcc/gcc-cross-canadian_debian.bb
meta-environment-qemuarm64                                      meta                    1.0-r8                          /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-core/meta/meta-environment.bb
nativesdk-gnu-config                                            meta                    20181128+gitAUTOINC+058639be22-r0       /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/gnu-config/gnu-config_git.bb
nativesdk-libnsl2                                               meta                    1.2.0+gitAUTOINC+37c5ffe303-r0  /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-extended/libnsl/libnsl2_git.bb
nativesdk-libsolv                                               meta                    0.7.3-r0                        /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-extended/libsolv/libsolv_0.7.3.bb
nativesdk-makedevs                                              meta                    1.0.1-r0                        /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/makedevs/makedevs_1.0.1.bb
nativesdk-meson                                                 meta                    0.49.2-r0                       /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/meson/nativesdk-meson_0.49.2.bb
nativesdk-opkg                                                  meta                    1:0.4.0-r0                      /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/opkg/opkg_0.4.0.bb
nativesdk-packagegroup-sdk-host                                 meta                    1.0-r12                         /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-core/packagegroups/nativesdk-packagegroup-sdk-host.bb
nativesdk-python3-setuptools                                    meta                    40.8.0-r0                       /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/python/python3-setuptools_40.8.0.bb
nativesdk-qemu                                                  meta                    3.1.0-r0                        /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/qemu/qemu_3.1.0.bb
nativesdk-qemu-helper                                           meta                    1.0-r9                          /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/qemu/nativesdk-qemu-helper_1.0.bb
nativesdk-sdk-provides-dummy                                    meta                    1.0-r0                          /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-core/meta/nativesdk-sdk-provides-dummy.bb
nativesdk-unfs3                                                 meta                    0.9.22.r497-r0                  /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-devtools/unfs3/unfs3_0.9.22.r497.bb
packagegroup-cross-canadian-qemuarm64                           meta                    1.0-r0                          /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-core/packagegroups/packagegroup-cross-canadian.bb
```

### check target sdk

Check target sdk.

```
$ ./check-packages.py whitelist/recipes-whitelist.txt core-image-minimal -s -m ../emlinux/build/tmp-glibc/deploy/sdk/emlinux-glibc-x86_64-core-image-minimal-aarch64-toolchain-2.0.target.manifest
==== Packages not built from debian source ====
package name                                                    layer                   version                         bbfile path
packagegroup-core-standalone-sdk-target                         meta                    1.0-r8                          /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-core/packagegroups/packagegroup-core-standalone-sdk-target.bb
target-sdk-provides-dummy                                       meta                    1.0-r0                          /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-core/meta/target-sdk-provides-dummy.bb
xz                                                              meta                    5.2.4-r0                        /home/masami/projects/emlinux/emlinux/repos/poky/meta/recipes-extended/xz/xz_5.2.4.bb
```
