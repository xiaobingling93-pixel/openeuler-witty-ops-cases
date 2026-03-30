# import torch npu时报错“ImportError：libtorch_npu.so: undefined symbol：_ZNK”

## 内核版本


## 问题现象
在执行 import torch npu 时出现 ImportError，具体报错信息为：libtorch_npu.so: undefined symbol: _ZNK5torch******。

## 问题根因
torch 和 torch_npu 安装的版本不匹配，导致动态链接库中符号未定义。

## 解决方案
重新安装与当前环境配套的 torch 和 torch_npu 版本，确保两者版本兼容。

