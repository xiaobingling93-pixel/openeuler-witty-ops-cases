# Python配置过程中报错

## 内核版本


## 问题现象
运行 ./configure 后报错，报错信息为：“gcc: error: directory": No such file or directory”。

## 问题根因
Python老版本的bug。

## 解决方案
执行以下命令：SVNVERSION=not-found ./configure

