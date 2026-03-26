# 在模型运行时遇到报错“RuntimeError: could not create a primitive descriptor for a matmul primitive”

## 内核版本


## 问题现象
在模型运行时，调用torch.nn.Linear层执行F.linear计算时，出现报错：RuntimeError: could not create a primitive descriptor for a matmul primitive。具体发生在PyTorch 2.1.0版本中，当线性层的out_features为1时，在aarch64架构的CPU上触发该错误。

## 问题根因
该问题是由于PyTorch 2.1.0版本自身在aarch64架构下对out_features为1的matmul操作支持不完善所导致，属于PyTorch框架的已知问题（参考GitHub issue #110149）。

## 解决方案
将PyTorch从2.1.0版本升级至2.2.0或更高版本即可解决此问题。

