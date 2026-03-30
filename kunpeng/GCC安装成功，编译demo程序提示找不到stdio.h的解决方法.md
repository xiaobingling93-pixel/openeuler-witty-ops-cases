# GCC安装成功，编译demo程序提示找不到stdio.h的解决方法

## 内核版本


## 问题现象
在使用openEuler-22.03-LTS-SP3-aarch64.qcow2.xz镜像时，尽管GCC已安装成功，但在编译包含#include <stdio.h>的C语言demo程序时，报错提示“fatal error: stdio.h: No such file or directory”。

## 问题根因
stdio.h头文件由glibc-devel包提供，系统未安装该开发包导致编译器无法找到标准库头文件。

## 解决方案
执行命令安装glibc-devel包：yum install glibc-devel -y，然后重新编译程序即可。

