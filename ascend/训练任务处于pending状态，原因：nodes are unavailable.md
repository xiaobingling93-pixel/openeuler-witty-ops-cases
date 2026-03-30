# 训练任务处于pending状态，原因：nodes are unavailable

## 内核版本


## 问题现象
下发vcjob任务后，训练任务一直未运行。通过kubectl get pod --all-namespaces查看发现Pod处于pending状态；进一步通过kubectl describe pod查看事件信息，显示错误：all nodes are unavailable: 1 node annotations(7) not same node idle(8)。

## 问题根因
该节点的未使用NPU数目与configmap中记录的未使用NPU数目不一致，导致Volcano调度器认为系统处于不稳定状态，拒绝分配NPU资源。根本原因主要是Ascend Device Plugin启动方式存在问题，也可能在任务量极大导致K8s响应缓慢时加剧此问题。

## 解决方案
重新安装Ascend Device Plugin，具体操作可参考《MindCluster 集群调度安装指南》中“安装部署 > 手动安装 > Ascend Device Plugin”章节。

