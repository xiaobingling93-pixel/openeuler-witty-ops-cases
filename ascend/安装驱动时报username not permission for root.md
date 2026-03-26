# 安装驱动时报username not permission for root

## 内核版本


## 问题现象
安装驱动时出现错误提示：[ERROR]ERR_NO:0x0091;ERR_DES:username not permission for root, check /etc/ascend_install.info。

## 问题根因
设备已安装过驱动。

## 解决方案
将安装方式的--full参数改为--upgrade。

