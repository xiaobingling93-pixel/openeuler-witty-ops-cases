# 模型训练时报错“NotImplementedError: Cannot convert a symbolic Tensor to a numpy array”

## 内核版本


## 问题现象
部分模型训练时，出现报错“NotImplementedError: Cannot convert a symbolic Tensor to a numpy array”，导致模型训练失败。

## 问题根因
numpy的版本过高，不支持当前模型进行训练。

## 解决方案
卸载当前版本的numpy，安装1.19.5版本的numpy，重新启动训练任务。

