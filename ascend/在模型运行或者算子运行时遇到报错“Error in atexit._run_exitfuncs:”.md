# 在模型运行或者算子运行时遇到报错“Error in atexit._run_exitfuncs:”

## 内核版本


## 问题现象
在模型或算子运行结束时，出现报错：Error in atexit._run_exitfuncs: Traceback (most recent call last): File "/root/archiconda3/envs/***/lib/python3.7/site-packages/torch/__init__.py", line 429, in _npu_shutdown torch._C._npu_shutdown() RuntimeError

## 问题根因
在torch初始化时未通过torch_npu.npu.device(id)指定NPU设备，默认使用device 0。若后续直接在其他NPU设备（如device 1）上创建tensor，则会在程序退出时因设备不一致导致_npu_shutdown失败，从而抛出RuntimeError。

## 解决方案
在调用NPU设备之前，通过torch_npu.npu.set_device(device)显式指定要使用的NPU设备ID，确保初始化与实际使用的设备一致。

