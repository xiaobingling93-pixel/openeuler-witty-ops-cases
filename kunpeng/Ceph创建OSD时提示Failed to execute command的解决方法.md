# Ceph创建OSD时提示Failed to execute command的解决方法

## 内核版本


## 问题现象
Ceph集群在重启OSD节点后，部分OSD状态变为down，测试工具报错“Slave hd2-0 prematurely terminated”，无法正常进行读写测试。

## 问题根因
“osd_memory_target”的值不是官方默认的4GB（4294967296），导致OSD进程在获取内存时失败。

## 解决方案
在ceph.conf文件中显式设置“osd_memory_target = 4294967296”，然后使用命令“ceph-deploy --overwrite-conf admin ceph1 ceph2 ceph3 client1 client2 client3”将配置推送到所有节点，最后执行“systemctl restart ceph.target”重启集群。

