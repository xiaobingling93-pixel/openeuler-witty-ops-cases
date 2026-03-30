# 启动StreamServer服务时，发生coredump

## 内核版本


## 问题现象
启动StreamServer服务时，出现coredump提示。

## 问题根因
StreamServer解密功能所依赖的kmc模块要求环境中不可以存在多版本Openssl。不同版本的openssl库函数中的结构体不同，因此可能会触发coredump。

## 解决方案
检查环境中是否存在多版本的Openssl。若存在，建议将多版本的Openssl归一为单一版本。

