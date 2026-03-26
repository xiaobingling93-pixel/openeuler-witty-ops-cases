# 麒麟V10 SP2系统下安装编译Redis时提示找不到-latomic的解决方法

## 内核版本


## 问题现象
在麒麟V10 SP2系统下安装编译Redis时，链接阶段报错：/usr/bin/ld: 找不到 -latomic，导致编译失败。

## 问题根因
系统未安装libatomic库，而Redis在编译时依赖该库提供的原子操作功能以确保多线程环境下的数据一致性。

## 解决方案
执行命令 yum -y install libatomic 安装libatomic库，然后重新编译安装Redis即可解决问题。

