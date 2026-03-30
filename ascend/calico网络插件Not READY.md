# calico网络插件Not READY

## 内核版本


## 问题现象
通过kubectl get pod -A查看calico网络插件时，READY一栏显示为“0/1”，表示calico插件未就绪。

## 问题根因
物理机网络段和配置的容器网络段冲突，或者物理机处于复杂网络环境中，导致calico无法正确识别master和worker节点的有效网卡。

## 解决方案
检查物理机网络是否与容器网段冲突，若存在冲突，需重新初始化Kubernetes集群，并修改pod-network-cidr参数为不冲突的网段。初始化后同步修改calico配置：在calico启动yaml中设置CALICO_IPV4POOL_CIDR为新的网段，并增加IP_AUTODETECTION_METHOD配置，其value值设为“can-reach={masterIP}”，其中masterIP为Kubernetes管理节点的物理机IP地址。

