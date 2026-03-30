# 动态shape推理申请内存失败

## 内核版本


## 问题现象
模型推理过程中，申请了大小为0的内存，日志报错信息中包含以下关键信息：[INFO] ASCENDCL ****** start to execute aclrtMalloc, size = 0；[ERROR] ASCENDCL ****** malloc size must be greater than zero。

## 问题根因
模型为动态shape模型，模型的输出shape中含有-1，直接调用aclmdlGetOutputSizeByIndex接口取到的size为0，导致申请了大小为0的内存而失败。

## 解决方案
参考《应用软件开发指南 (C&C++)》的“模型动态Shape输入推理”章节内容处理。在aclmdlGetOutputSizeByIndex取到size为0时，用户需要预估一块较大的内存。

