# 运行configure时报错

## 内核版本


## 问题现象
运行configure时报错，报错信息为：“error: external libxc support does not work”。

## 问题根因
配置参数 --with-libxc-libs= 未按照正确顺序书写。

## 解决方案
在编译安装时按顺序添加参数：--with-libxc-libs=-lxcf90 -lxc。

