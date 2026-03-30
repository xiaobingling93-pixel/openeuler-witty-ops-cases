# Ceph OSD偶尔收到SIGHUP信号的解决方法

## 内核版本


## 问题现象
在Ceph集群进行读写性能测试后重启OSD节点时，部分OSD进程无法正常启动，导致测试工具报错“Slave hd2-0 prematurely terminated”，同时Ceph集群状态显示部分OSD为down状态。

## 问题根因
“osd_memory_target”的值不是官方默认的4GB（4294967296字节），导致OSD进程在分配内存时失败，从而引发进程异常终止。

## 解决方案
1. 通过命令“ceph --admin-daemon /var/run/ceph/ceph-osd.0.asoc config show | grep memory”确认当前osd_memory_target配置值；
2. 在ceph.conf文件中显式设置“osd_memory_target = 4294967296”以限制每个OSD使用4GB内存；
3. 使用“ceph-deploy --overwrite-conf admin ceph1 ceph2 ceph3 client1 client2 client3”将修改后的配置文件同步到所有节点；
4. 执行“systemctl restart ceph.target”重启Ceph集群使配置生效。

