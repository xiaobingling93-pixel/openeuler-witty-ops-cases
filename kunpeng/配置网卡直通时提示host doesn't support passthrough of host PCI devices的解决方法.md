# 配置网卡直通时提示host doesn't support passthrough of host PCI devices的解决方法

## 内核版本


## 问题现象
虚拟机配置SRIOV网卡直通时，提示"host doesn't support passthrough of host PCI devices"。

## 问题根因
虚拟机配置网卡直通必须开启SMMU/IOMMU，而当前系统未启用该功能。

## 解决方案
1. 打开grub2.cfg文件：vim /etc/grub.cfg；
2. 添加内核启动参数：iommu.passthrough=1；
3. 保存并退出编辑（按“Esc”键，输入:wq!，按“Enter”）；
4. 重启服务器使配置生效。
参考图示：![](/doc_center/source/zh/kunpengwebs/troubleshooting/trouble/zh-cn_image_0000001171661564.png)

