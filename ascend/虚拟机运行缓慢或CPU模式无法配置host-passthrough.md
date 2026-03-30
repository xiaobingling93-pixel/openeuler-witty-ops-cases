# 虚拟机运行缓慢或CPU模式无法配置host-passthrough

## 内核版本


## 问题现象
虚拟机创建成功后运行速度缓慢，且在尝试将CPU模式配置为host-passthrough时出现报错。

## 问题根因
可能原因一：默认的开源QEMU配置中kvm配置项为auto，使用默认参数创建虚拟机时可能未开启KVM硬件加速。可能原因二：当前环境CPU不支持KVM硬件加速功能。

## 解决方案
1. 修改QEMU源码后重新构建并安装QEMU。2. 修改目标虚拟机的配置文件：将domain type设为'kvm'，cpu mode设为'host-passthrough'。具体步骤包括：查询虚拟机列表，必要时关闭虚拟机，使用virsh edit命令编辑虚拟机配置文件，并按要求修改domain类型和CPU模式。

