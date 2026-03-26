# 模型训练时未使用配套PyTorch或Python版本，报错“E1017”

## 内核版本


## 问题现象
在模型训练过程中出现“E1017”报错，具体表现为：训练开始后不久进程崩溃，报错信息包含“failed (exitcode: -11) local_rank:0”以及“an autograd kernel was not registered to the Autograd key(s) but we are trying to backprop through it. This may lead to silently incorrect behavior.”

## 问题根因
使用了未适配的PyTorch和Python版本进行模型训练，导致框架与昇腾NPU后端不兼容，从而引发功能错误和训练失败。

## 解决方案
根据模型使用说明中推荐的PyTorch、Python等配套版本重新准备运行环境，确保所用软件版本与昇腾CANN及硬件平台兼容，以保障训练功能正常、性能和精度达标。

