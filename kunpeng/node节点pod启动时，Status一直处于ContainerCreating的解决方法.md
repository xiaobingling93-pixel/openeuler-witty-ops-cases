# node节点pod启动时，Status一直处于ContainerCreating的解决方法

## 内核版本


## 问题现象
kubectl get pod -o wide发现pod的状态一直显示为ContainerCreating。查看日志，日志中显示如下信息：network: failed to set bridge addr: "cni0" already has an IP address different from 10.244.2.1/24

## 问题根因
Node之前反复添加过集群，导致CNI网络配置冲突。

## 解决方案
1. 在Node上执行如下操作：
kubeadm reset
systemctl stop kubelet
systemctl stop docker
rm -rf /var/lib/cni/
rm -rf /var/lib/kubelet/*
rm -rf /etc/cni/
ifconfig cni0 down
ifconfig flannel.1 down
ifconfig docker0 down
ip link delete cni0
ip link delete flannel.1
systemctl start docker
2. Node上重新运行kubeadm join加入集群。
3. 重新尝试创建pod容器。

