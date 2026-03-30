# 通过设置Max Payload Size提升h2d带宽性能

## 内核版本


## 问题现象
使用Ascend-dmi测试Atlas A2训练系列产品带宽值不达标。

## 问题根因
Atlas A2训练系列产品ARM架构在HOST侧的Max Payload Size默认值为256B，未达到最佳带宽性能所需的512B。

## 解决方案
登录iBMC界面，通过虚拟控制台进入BIOS设置，在Advanced > PCIe Config中，依次进入每个CPU的PCIe Configuration和Port 0，将Max Payload Size从默认的256B修改为512B，保存并重启服务器。

