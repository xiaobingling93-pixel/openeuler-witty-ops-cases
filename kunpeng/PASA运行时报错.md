# PASA运行时报错

## 内核版本


## 问题现象
PASA运行时报错，报错信息类似：“Can't locate URI/Escape.pm in @INC”。

## 问题根因
perl缺少URI模块。

## 解决方案
1. 使用PuTTY工具，以root用户登录服务器。
2. 执行以下命令解压URI：tar -xvf URI-1.35.tar.gz
3. 执行以下命令进入解压目录：cd URI-1.35
4. 执行以下命令编译安装：perl Makefile.PL、make、make install

