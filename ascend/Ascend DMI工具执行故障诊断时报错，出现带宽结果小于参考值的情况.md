# Ascend DMI工具执行故障诊断时报错，出现带宽结果小于参考值的情况

## 内核版本


## 问题现象
Ascend DMI工具执行故障诊断时报错，提示带宽测试结果小于参考值。

## 问题根因
当前环境上驱动的ECC功能为开启状态，导致带宽测试结果不达标。

## 解决方案
1. 执行命令 'npu-smi info -t ecc-enable -i 0' 查看驱动ECC功能状态；2. 若状态为“True”，执行 'npu-smi set -t ecc-enable -i 0 -d 0' 关闭ECC功能；3. 再次执行 'ascend-dmi --dg' 进行故障诊断，确认带宽测试结果恢复正常。

