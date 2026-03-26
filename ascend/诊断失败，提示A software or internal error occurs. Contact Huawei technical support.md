# 诊断失败，提示A software or internal error occurs. Contact Huawei technical support

## 内核版本
23.0.0及以上

## 问题现象
使用Ascend DMI工具执行Aicore诊断时失败，提示“A software or internal error occurs. Contact Huawei technical support”。

## 问题根因
可能原因包括：驱动固件版本低于23.0.0、MCU版本未升级至23.0.0及以上、或未安装kernel包。

## 解决方案
1. 使用ascend-dmi -c命令检查驱动固件版本是否为23.0.0及以上；2. 使用npu-smi upgrade -b mcu -i $i（$i为设备ID）检查MCU版本是否为23.0.0及以上；3. 使用find /usr/local/Ascend/ -name kernel命令确认kernel包是否已安装，通常位于/usr/local/Ascend/ascend-toolkit/<version>/opp/built-in/op_impl/ai_core/tbe/kernel路径下。

