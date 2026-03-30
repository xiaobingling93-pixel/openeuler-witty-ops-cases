# 在进行跨平台模型加载时遇到报错ModuleNotFoundError: No module named 'torch_npu'

## 内核版本


## 问题现象
在进行跨平台模型加载时，调用torch.load()报错：ModuleNotFoundError: No module named 'torch_npu'。

## 问题根因
在保存模型时，没有将模型转换为CPU模型，或者保存了NPU optimizer的信息，导致模型文件依赖torch_npu模块。

## 解决方案
在NPU环境中加载模型权重文件中的参数，然后将其转移到CPU上重新保存，使新文件不依赖torch_npu包。示例代码：tmp = torch.load('xxx.pt', map_location='cpu'); torch.save(tmp, 'new_xxx.pt')。

