# 在模型运行或者算子运行时遇到报错“RuntimeError: ExchangeDevice:”

## 内核版本


## 问题现象
在模型或算子运行过程中，出现如下报错：RuntimeError: ExchangeDevice:/home/***/pytorch/c10/npu/sys_ctrl/npu_sys_ctrl.cpp:56 NPU error, error code is 500000；以及RuntimeError: npuSynchronizeDevice:/***/code/pytorch/c10/npu/NPUStream.cpp:776 NPU error, error code is 200005。

## 问题根因
在一个线程内只能调用一个NPU设备，当尝试在同一进程中切换不同的NPU device时，会触发该错误。

## 解决方案
检查代码中调用 torch_npu.npu.set_device(device)、tensor.to(device) 或 model.to(device) 的位置，确保在同一个线程内前后使用的 device 名称一致。对于多线程场景（如多卡训练），每个线程也应固定使用一个 NPU device，不得在同一线程中切换设备。

