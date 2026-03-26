# Python-3.8.2安装编译时报错

## 内核版本


## 问题现象
Python-3.8.2安装编译过程中，报错：“ModuleNotFoundError: No module named '_ctypes'”。

## 问题根因
由于在CentOS7系统中没有安装外部函数库（libffi）的开发链接库软件包，导致编译时缺少_ctypes模块。

## 解决方案
在Python-3.8.2安装编译之前，执行命令 yum install libffi-devel -y 安装libffi-devel包。

