# 删除存储卷时提示volume '25.img' is still being allocated的解决方法

## 内核版本


## 问题现象
删除存储卷时提示“volume '25.img' is still being allocated”。

## 问题根因
存储卷在创建中，无法删除。

## 解决方案
重启libvirtd服务即可。具体步骤为：1. 停止libvirtd服务（systemctl stop libvirtd）；2. 启动libvirtd服务（systemctl start libvirtd）。

