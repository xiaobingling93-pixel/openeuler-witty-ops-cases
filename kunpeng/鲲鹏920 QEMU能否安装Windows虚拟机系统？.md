# 鲲鹏920 QEMU能否安装Windows虚拟机系统？

## 内核版本


## 问题现象
用户希望在基于鲲鹏920（ARM架构）的服务器上通过QEMU安装Windows虚拟机系统。

## 问题根因
鲲鹏920服务器采用ARM架构，而当前没有正式版本的Windows虚拟机系统支持在ARM架构上通过QEMU运行；若需运行Windows虚拟机，必须使用ARM版本的Windows，并对QEMU启动参数进行适配修改。

## 解决方案
1. 鲲鹏920服务器目前不支持安装常规x86版本的Windows虚拟机系统。2. 如确需在ARM架构服务器上启动Windows虚拟机，应安装ARM版本的Windows系统，并相应调整QEMU的启动参数以适配ARM架构。

