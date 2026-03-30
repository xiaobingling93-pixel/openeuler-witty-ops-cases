# 使用QEMU安装OS时，使能KVM后无响应的解决方法

## 内核版本


## 问题现象
编译安装qemu-4.2.0后，使用QEMU安装OS时，使能KVM后无响应，禁用KVM时则能正常进入安装界面。

## 问题根因
在CentOS 7.6系统中出现coredump提示：'qemu-system-aarch64: PMU: KVM_SET_DEVICE_ATTR: Invalid argument' 和 'qemu-system-aarch64: failed to set irq for PMU'，表明KVM在设置PMU设备属性时因参数无效而失败，导致QEMU崩溃。

## 解决方案
在CentOS 7.7系统的启动命令中添加-machine gic-version=3，成功进入安装界面。

