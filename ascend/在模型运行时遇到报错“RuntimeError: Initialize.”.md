# 在模型运行时遇到报错“RuntimeError: Initialize.”

## 内核版本


## 问题现象
在模型运行时出现报错：RuntimeError: Initialize:/home/***/code/pytorch/c10/npu/sys_ctrl/npu_sys_ctrl.cpp:44 NPU error, error code is 500000。

## 问题根因
NPU设备初始化失败，系统在拉起NPU设备时发生错误。

## 解决方案
1. 重启服务器和所有NPU设备；2. 若问题未解决，检查driver和firmware版本是否匹配；3. 若不匹配，更换正确版本的driver和firmware；4. 若仍无法解决，联系华为工程师。

