# 代码编译脚本有char数据类型符号的解决方法

## 内核版本


## 问题现象
编译时出现告警信息：warning: comparison is always false due to limited range of data type。

## 问题根因
char变量在不同CPU架构下默认符号不一致，在x86架构下为signed char，在ARM64平台为unsigned char，导致移植到ARM64平台时出现逻辑错误或编译告警。

## 解决方案
在编译选项中加入“-fsigned-char”选项，指定ARM64平台下的char为有符号数。

