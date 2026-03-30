# pip3 install numpy报错

## 内核版本


## 问题现象
在安装依赖时，执行 pip3 install numpy 命令报错：“Could not build wheels for numpy which use PEP 517 and cannot be installed directly”。

## 问题根因
CentOS等系统默认安装的GCC版本较低，导致无法正确编译numpy。

## 解决方案
执行以下命令安装：export CFLAGS=-std=c99 && pip3 install numpy==1.17.2

