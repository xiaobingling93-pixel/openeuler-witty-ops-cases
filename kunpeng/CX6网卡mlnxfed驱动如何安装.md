# CX6网卡mlnxfed驱动如何安装

## 内核版本


## 问题现象
用户需要在系统中安装CX6网卡的MLNX_OFED驱动，但缺乏明确的操作指引。

## 问题根因


## 解决方案
1. 解压驱动安装包（如MLNX_OFED_LINUX-5.5-1.0.3.2-openeuler20.03-aarch64.tgz）；2. 安装依赖包（如perl、pciutils、python、gcc-gfortran等）；3. 执行./mlnxofedinstall进行驱动安装；4. 重启服务器；5. 配置OpenSM虚拟化支持（设置virt_enabled为2）；6. 使用mst start开启SR-IOV，并通过mlxconfig设置SRIOV_EN和NUM_OF_VFS参数；7. 执行mlxfwreset重置设备；8. 设置VF数量（如echo 2 > /sys/class/net/enp125s0f3/device/sriov_numvfs）；9. 使用ifconfig、ip a、lspci、ibdev2netdev等命令验证安装是否成功。

