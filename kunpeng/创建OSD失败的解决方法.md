# 创建OSD失败的解决方法

## 内核版本


## 问题现象
创建OSD失败，报错信息为：RuntimeError: command returned non-zero exit status: 1，具体命令为 /usr/sbin/ceph-volume --cluster ceph lvm create --bluestore --data /dev/nvme0n1p1，最终提示 Failed to create 1 OSDs。

## 问题根因
OSD所依赖的LVM创建失败，原因是Ceph逻辑卷的设备映射（DM）未被清除。执行 lvs 命令无法看到Ceph逻辑卷，但 lsblk 命令却能发现该逻辑卷，说明存在残留的DM映射。

## 解决方案
清除残留的逻辑卷DM映射，执行以下命令：
1. 使用 dmsetup info -C 查看当前的DM映射；
2. 使用 dmsetup remove [dm_map_name] 删除对应的映射。

