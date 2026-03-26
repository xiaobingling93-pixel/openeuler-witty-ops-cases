# 编译abinit时make报错

## 内核版本


## 问题现象
编译abinit时make报错，报错信息为：“Error: Line truncated at (1) [-Werror=line-truncation]”。

## 问题根因
此错误是因为代码中未限制132个字符。

## 解决方案
需要在编译安装的FCFLAGS="-g -O2 -ffree-line-length-none"中增加-ffree-line-length-none。

