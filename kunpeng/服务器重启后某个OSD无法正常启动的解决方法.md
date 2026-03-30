# 服务器重启后某个OSD无法正常启动的解决方法

## 内核版本


## 问题现象
Ceph集群在重启OSD节点后，部分OSD状态变为down，导致测试工具报错“Slave hd2-0 prematurely terminated”，无法继续进行读写测试。

## 问题根因
“osd_memory_target”的值不是官方默认的4GB（4294967296字节），导致OSD进程在启动时分配内存失败。

## 解决方案
1. 通过命令 `ceph --admin-daemon /var/run/ceph/ceph-osd.0.asoc config show | grep memory` 确认当前osd_memory_target配置异常；
2. 在ceph.conf文件中显式设置 `osd_memory_target = 4294967296`；
3. 使用 `ceph-deploy --overwrite-conf admin ceph1 ceph2 ceph3 client1 client2 client3` 将配置同步到所有节点；
4. 执行 `systemctl restart ceph.target` 重启集群服务。

