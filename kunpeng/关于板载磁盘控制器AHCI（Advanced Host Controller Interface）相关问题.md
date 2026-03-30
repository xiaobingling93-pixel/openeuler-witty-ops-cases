# 关于板载磁盘控制器AHCI（Advanced Host Controller Interface）相关问题

## 内核版本


## 问题现象
用户对鲲鹏920机型板载磁盘控制器AHCI直出的连接方式存在疑问，包括是否指硬盘背板直连CPU，以及是否可以在不配置RAID卡的情况下通过SATA线缆将前置直通背板连接到主板。

## 问题根因
AHCI直出是指主板上的SATA控制器（集成在CPU或芯片组中）直接管理SATA硬盘，无需经过RAID卡或HBA卡；硬盘背板可通过SATA线缆连接至主板AHCI控制器，并通过PCIe总线与CPU通信。

## 解决方案
可以不配置RAID卡，硬盘背板通过SATA线缆连接到主板上的AHCI控制器即可实现直通。AHCI控制器通常集成在CPU或芯片组中，通过主板PCB走线连接到SATA接口（可能位于主板或背板上），无需第三方控制器中转。

