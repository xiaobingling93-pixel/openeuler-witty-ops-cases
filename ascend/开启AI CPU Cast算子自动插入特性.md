# 开启AI CPU Cast算子自动插入特性

## 内核版本


## 问题现象
MatrixInverse算子的输入x不支持float16的数据类型，导致模型编译失败。

## 问题根因
AI CPU算子（如MatrixInverse）在遇到不支持的数据类型（如float16）时无法直接处理，需通过数据类型转换才能兼容运行。

## 解决方案
1. 打开AutoCast开关：修改Ascend CANN工具包中的init.conf文件，将AutoCastMode参数设为1；2. 修改算子信息库，在MatrixInverse算子的输入和输出配置中添加对DT_FLOAT16的支持，并分别指定srcAutoCastType和dstAutoCastType，以自动插入float16与float32之间的Cast算子进行类型转换。

