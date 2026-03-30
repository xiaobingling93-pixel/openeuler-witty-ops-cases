# Euler OS下编译fio 2.1.10提示collect2: error: ld returned 1 exit status的解决方法

## 内核版本


## 问题现象
在鲲鹏服务器上安装Euler for ARM系统，编译fio 2.1.10执行make后提示“collect2: error: ld returned 1 exit status”。

## 问题根因
os-linux.h文件中缺少对头文件<sys/sysmacros.h>的包含，导致链接阶段失败。

## 解决方案
1. 修改os-linux.h，在文件中添加头文件#include <sys/sysmacros.h>；2. 重新执行make && make install，编译安装成功。

