# Arm场景将8张昇腾AI处理器直通给虚拟机后使用npu-smi工具只能查询到5张昇腾AI处理器

## 内核版本


## 问题现象
在Arm架构下，将8张昇腾AI处理器通过PCIe直通方式分配给虚拟机后，使用npu-smi工具仅能识别到5张处理器。通过执行'dmesg | grep "BAR 4"'命令可观察到相关错误信息，表明存在PCIe地址空间分配失败的问题。

## 问题根因
默认的开源QEMU配置中，PCIe域的地址空间被限制为512GB。每张昇腾AI处理器的BAR4资源需求为64GB，8张卡共需512GB，再加上虚拟机自身已占用的部分地址空间，导致无法为所有设备分配足够的PCIe地址空间，从而造成部分设备无法被识别。

## 解决方案
修改QEMU源码中的hw/arm/virt.c文件，将extended_memmap数组中VIRT_HIGH_PCIE_MMIO项的地址空间大小从512 GiB调整为1024 GiB，然后重新编译并安装QEMU。具体修改为：将'[VIRT_HIGH_PCIE_MMIO] = { 0x0, 512 * GiB }'改为'[VIRT_HIGH_PCIE_MMIO] = { 0x0, 1024 * GiB }'。

