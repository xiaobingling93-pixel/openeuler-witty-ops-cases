# 如何关闭SMMU？

## 内核版本


## 问题现象
开启SMMU后内存访问会经过MMU模块地址转换，对性能存在影响。

## 问题根因


## 解决方案
1. 重启服务器过程中，按“Delete”键进入BIOS，选择“Advanced > MISC Config”，按“Enter”键进入。
2. 将“Support Smmu”设置为“Disable”。

