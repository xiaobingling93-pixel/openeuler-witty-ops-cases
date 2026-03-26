# 容器场景执行Aicore命令失败，plog日志报错，驱动故障码为46

## 内核版本


## 问题现象
在容器中使用Ascend DMI工具执行Aicore命令失败，plog日志中报错：[ERROR]...[dsmi_check_out_valid 243]recv msg data error code 46, recv msg data opcode 0x643；以及[dsmi_cmd_set_device_info 874]... dsmi_send_msg_rec_res failed, ret = 46。

## 问题根因
容器权限不足，导致调用驱动接口时失败，驱动返回错误码46。

## 解决方案
确保容器具有足够的权限访问昇腾设备驱动，例如以特权模式运行容器或正确挂载设备和驱动相关路径，并配置必要的设备访问权限。

