# CentOS系统下内存页Page Size如何从64K切换到4K？

## 内核版本
4.18.0-193.28.1.el8_2

## 问题现象
用户需要将CentOS系统下的内存页大小从默认的64KB切换为4KB，以满足特定应用或性能需求。

## 问题根因


## 解决方案
1. 查看当前内存页大小：执行 getconf PAGESIZE，确认为65536（即64KB）。
2. 下载对应版本的内核源码：wget https://git.centos.org/sources/kernel/c8/a857effa0971fa1b6790bf8df25f69dda20acdd3。
3. 解压并将源码移至 /usr/src 目录。
4. 安装编译依赖：yum install -y vim rpm-build net-tools bc xmlto asciidoc openssl-devel hmaccalc python-devel newt-devel perl elfutils-devel zlib-devel binutils-devel audit-libs-devel java-devel numactl-devel pciutils-devel ncurses-devel perl-ExtUtils-Embed git。
5. 进入内核源码目录，复制当前系统的 .config 文件：cp /boot/config-`uname -r` ./.config。
6. 使用 make menuconfig 修改 Page size：进入 Kernel Features → Page size（64KB），选择 4KB 并保存退出。
7. 验证 .config 中配置已更新：grep -i pages .config，确认 CONFIG_ARM64_4K_PAGES=y 且 CONFIG_ARM64_64K_PAGES 被注释。
8. 修改 Makefile 中的 EXTRAVERSION 字段以区分新内核版本。
9. 编译内核 RPM 包：make binrpm-pkg -j`nproc`，在交互提示中确认 Page size 为 4KB，并根据需要设置虚拟地址空间等选项。
10. 安装生成的 RPM 包：rpm -ivh /root/rpmbuild/RPMS/aarch64/kernel-4.18.0_3-7.aarch64.rpm。
11. 验证安装：rpm -qa | grep kernel。
12. 重启系统并从 GRUB 菜单选择新内核启动。
13. 检查内核版本：uname -a。
14. 验证 Page size 已变为 4096：getconf PAGESIZE。

