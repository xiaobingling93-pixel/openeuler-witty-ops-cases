# 配置网卡直通时提示host doesn't support passthrough of host PCI devices的解决方法（虚拟化）

## 内核版本


## 问题现象
虚拟机配置SRIOV网卡直通时，提示"host doesn't support passthrough of host PCI devices"。

## 问题根因
虚拟机配置网卡直通必须开启SMMU/IOMMU，但当前系统未启用该功能。

## 解决方案
1. 修改BIOS配置：进入BIOS->Advanced->MISC Config->Support Smmu，将Support Smmu设置为Enabled。
2. 编辑grub2配置文件：执行 vi /etc/grub2-efi.cfg，按“i”进入编辑模式，在内核启动参数中添加 iommu.passthrough=1。
3. 保存并退出：按“Esc”键，输入:wq!，按“Enter”保存退出。
4. 重启服务器使配置生效。
参考图片：/doc_center/source/zh/kunpengcpfs/troubleshooting/trouble/zh-cn_image_0000001564911862.png

