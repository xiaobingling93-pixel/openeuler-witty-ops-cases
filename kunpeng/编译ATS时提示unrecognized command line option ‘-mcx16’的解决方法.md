# 编译ATS时提示unrecognized command line option ‘-mcx16’的解决方法

## 内核版本


## 问题现象
在GCC版本为8.4.1的情况下，执行ATS 8.0.5的make编译时，提示“unrecognized command line option ‘-mcx16’”错误。

## 问题根因
GCC 8.4.1版本在编译时默认包含针对x86架构的‘-mcx16’编译选项，而该选项在ARM架构上不被支持，导致编译失败。

## 解决方案
进入trafficserver-8.0.5源码目录，使用命令`sed -i "s/\ -mcx16//g" $(find -name Makefile)`删除所有Makefile文件中的‘-mcx16’选项，然后执行`make clean`和`make -j60`重新编译安装。

