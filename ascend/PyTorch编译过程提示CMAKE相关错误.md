# PyTorch编译过程提示CMAKE相关错误

## 内核版本


## 问题现象
PyTorch编译时cmake依赖提示找不到包，或报错cmake版本过低。

## 问题根因
系统中缺少cmake包，或已安装的cmake版本低于编译PyTorch所需的最低版本（如3.12.0）。

## 解决方案
方法一：通过官方安装脚本安装指定版本cmake。根据系统架构（x86_64或aarch64）下载对应脚本（如cmake-3.12.0-Linux-{arch}.sh），执行安装后设置软链接至/usr/bin/cmake，并验证版本。方法二：从源码编译安装cmake。下载cmake-3.12.0.tar.gz，解压后执行./configure --prefix=/usr/local/cmake、make && make install，再设置软链接并验证版本。

