# 替换CANN包中的.so文件后，执行ATC模型转换报错：baoundefined symbol

## 内核版本


## 问题现象
替换CANN包中的.so文件后，执行ATC模型转换时报undefined symbol错误。

## 问题根因
更新的.so文件与当前CANN版本不匹配，导致符号未定义。

## 解决方案
编译.so文件时需确保与实际使用环境（包括CANN版本）保持一致。

