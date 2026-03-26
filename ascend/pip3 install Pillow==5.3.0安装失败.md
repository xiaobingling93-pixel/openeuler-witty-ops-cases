# pip3 install Pillow==5.3.0安装失败

## 内核版本


## 问题现象
执行 pip3 install Pillow==5.3.0 命令时安装失败。

## 问题根因
系统缺少必要的依赖库，包括 libjpeg、python-devel、zlib-devel 和 libjpeg-turbo-devel。

## 解决方案
根据操作系统类型安装缺失的依赖库：对于 CentOS/EulerOS/Tlinux/BClinux/Suse 系统，运行 yum install libjpeg python-devel zlib-devel libjpeg-turbo-devel；对于 Ubuntu/Debian/UOS 系统，运行 apt-get install libjpeg python-devel zlib-devel libjpeg-turbo-devel。

