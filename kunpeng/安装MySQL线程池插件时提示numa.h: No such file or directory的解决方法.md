# 安装MySQL线程池插件时提示numa.h: No such file or directory的解决方法

## 内核版本


## 问题现象
安装MySQL 8.0.25线程池插件过程中执行make命令时，提示“numa.h: No such file or directory”。

## 问题根因
MySQL程序在编译时未安装numactl依赖，导致无NUMA库加载，从而在执行make命令时报错。

## 解决方案
1. 安装numactl库：yum install -y numactl numactl-devel*；2. 重新编译MySQL，具体操作参见《MySQL 8.0.x 移植指南》。

