# K8s集群添加节点超时的解决方法

## 内核版本


## 问题现象
K8s集群添加节点超时，提示“execution phase kubelet-start”和“timed out waiting for the condition”。

## 问题根因
kubelet的服务状态已经受损。

## 解决方案
1. 执行以下命令重置kubeadm：
   kubeadm reset
   systemctl daemon-reload
   systemctl restart kubelet
2. 查看kubelet服务的状态，确认kubelet的服务状态已恢复：
   systemctl status kubelet

