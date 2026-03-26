# AscendCL案例推理失败问题分析googlenet_imagenet_dynamic_batch

## 内核版本


## 问题现象
在使用AscendCL进行googlenet模型多batchsize推理时，当batchsize大于2（如设置为4），推理结果异常。环境为CANN 6.0.RC1、Ubuntu 18.04、Python 3.7.5，通过指定动态batch_size="1,2,4"转换模型后，在运行时修改batchSize为4并增加对应输入数据，推理输出结果错误。

## 问题根因
后处理脚本中计算输出数据长度的逻辑错误。代码中使用outputDataSize/(sizeof(float)*2)来确定循环次数，其中固定除以2，而未根据实际batchSize动态调整。当batchSize为4时，模型总输出大小为16000字节（每batch输出4000字节，float类型占4字节，即每batch有1000个float），正确应为outputDataSize/(sizeof(float)*batchSize)，原逻辑导致读取数量翻倍，造成结果错误。

## 解决方案
将后处理脚本中循环判断条件由outputDataSize/(sizeof(float)*2)修改为outputDataSize/(sizeof(float)*batchSize)，使数据解析长度与实际batchSize匹配，从而正确提取每个batch的推理结果。

