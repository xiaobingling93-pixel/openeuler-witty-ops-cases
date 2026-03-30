# 使用MMEngine进行断点续训时报错

## 内核版本


## 问题现象
当PyTorch版本为2.1.0，在NPU上执行多卡训练，通过MMEngine进行断点续训时，报错：RuntimeError: Attempted to set the storage of a tensor on device "npu:X" to a storage on different device "npu:0"。

## 问题根因
PyTorch 2.1.0在多卡训练断点续训加载权重时，处理自定义设备会默认将权重都放到0卡上，导致其他卡上的tensor尝试使用位于npu:0的storage，从而引发设备不匹配错误。

## 解决方案
修改MMEngine中加载预训练权重的代码，将map_location参数从device改为包含具体LOCAL_RANK的设备标识。具体修改为：import os; device_id = os.environ['LOCAL_RANK']; device = get_device(); checkpoint = self.load_checkpoint(filename, map_location=f"{device}:{device_id}")。

