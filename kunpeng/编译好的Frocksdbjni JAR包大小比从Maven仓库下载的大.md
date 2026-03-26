# 编译好的Frocksdbjni JAR包大小比从Maven仓库下载的大

## 内核版本


## 问题现象
编译好的Frocksdbjni JAR包大小比从Maven仓库下载的大。

## 问题根因
JAR包内的librocksdbjni-linux64.so包含符号信息。

## 解决方案
执行如下命令去掉符号信息：strip。

