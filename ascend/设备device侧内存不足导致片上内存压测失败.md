# 设备device侧内存不足导致片上内存压测失败

## 内核版本


## 问题现象
Ascend DMI工具执行片上内存压力测试失败，提示Error occurred in HBM stress test on device 0，日志报错aclrtMalloc failed, error code: 207001。

## 问题根因
设备device侧内存不足或设备内存被占用。

## 解决方案
1. 执行npu-smi info查看内存是否被占用；2. 若内存被占满，可等待内存释放或执行命令npu-smi set -t reset -i $i -c 0（将$i替换为指定设备ID）复位芯片以释放内存。

