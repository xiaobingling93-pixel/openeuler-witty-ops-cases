# CUDA流同步操作报错

## 内核版本


## 问题现象
在使用PyTorch进行模型训练时，执行CUDA流同步操作报错，错误信息为：AssertionError: Torch not compiled with CUDA enabled。

## 问题根因
代码中未使用NPU对应的流同步方法，而是尝试调用CUDA相关的同步操作，但当前环境未启用CUDA支持。

## 解决方案
应使用NPU专用的流同步方法，具体代码为：stream = torch_npu.npu.current_stream()，然后调用 stream.synchronize()。

