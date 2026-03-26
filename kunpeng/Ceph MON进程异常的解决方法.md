# Ceph MON进程异常的解决方法

## 内核版本


## 问题现象
通过ceph -s观察到Ceph MON进程有slow ops，提示信息如下：HEALTH_WARN 376 slow ops, oldest one blocked for 894 sec, daemons [mon,ceph4,mon,ceph5,mon,ceph6] have slow ops. SLOW_OPS 376 slow ops, oldest one blocked for 894 sec, daemons [mon,ceph4,mon,ceph5,mon,ceph6] have slow ops.

## 问题根因
Ceph集群重新部署后，用原来Ceph集群的配置文件覆盖当前集群的配置文件，导致NUMA亲和性配置与实际情况不匹配。

## 解决方案
重新配置NUMA亲和性，根据实际情况修改ceph.conf中的NUMA亲和性配置，示例如下：
[osd.N]：
osd_numa_node = 1
public_network_interface = bond1
cluster_network_interface = bond1

