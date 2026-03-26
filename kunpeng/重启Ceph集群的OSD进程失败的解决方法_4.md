# 重启Ceph集群的OSD进程失败的解决方法

## 内核版本


## 问题现象
Ceph集群在一轮读写性能测试后，重启OSD节点时部分OSD状态变为down，测试工具报错“Slave hd2-0 prematurely terminated”，导致无法继续测试。

## 问题根因
osd_memory_target 的值不是官方默认的4GB（4294967296），导致OSD进程在获取内存时失败。

## 解决方案
在 ceph.conf 文件中显式设置 osd_memory_target = 4294967296，然后使用 ceph-deploy --overwrite-conf admin 命令将配置推送到所有节点，并执行 systemctl restart ceph.target 重启集群。

