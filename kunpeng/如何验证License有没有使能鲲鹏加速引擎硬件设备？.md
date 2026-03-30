# 如何验证License有没有使能鲲鹏加速引擎硬件设备？

## 内核版本


## 问题现象
安装完License之后，如何验证License有没有正常使能鲲鹏加速引擎硬件设备？

## 问题根因


## 解决方案
验证License有没有使能鲲鹏加速引擎硬件设备有以下两种方式：1. 在BIOS界面查看加速器状态。具体流程为：按Esc键进入BIOS界面，依次进入“Advanced > Accelerators Status”。如果已经安装成功则会显示相应信息。2. 在操作系统命令行界面中使用lspci命令进行查看。使用方法为：在环境中输入命令lspci | grep "xxx"（其中xxx为对应的驱动模块，取值可以是HPRE、SEC、RDE、ZIP），如果执行完命令后有信息输出则说明License已经正常使能鲲鹏加速引擎硬件设备。

