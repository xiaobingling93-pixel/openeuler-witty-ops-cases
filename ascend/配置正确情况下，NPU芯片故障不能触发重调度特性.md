# 配置正确情况下，NPU芯片故障不能触发重调度特性

## 内核版本


## 问题现象
在正确配置重调度特性时，偶尔出现NPU芯片故障但重调度特性不能正常触发；NPU芯片故障后，volcano-scheduler组件的Pod可能重启，且重调度后下发的任务Pod长时间处于pending状态；任务运行过程中，若在重启device-plugin后的一段时间内发生NPU芯片故障，会概率性导致NPU故障重调度不执行。

## 问题根因
NPU芯片故障后，Kubernetes将故障的NPU芯片移除。当Volcano尝试归还Pod占用的NPU芯片资源时，发现当前NPU芯片数量与K8s记录不一致，从而引发panic，导致Volcano将该node设置为notReady状态。在此状态下，若没有其他节点满足NPU资源要求，重调度后的新Pod会一直处于pending状态。该问题源于Volcano v1.4.0版本的缺陷。

## 解决方案
针对因Volcano panic导致的问题，可手动删除volcano-scheduler的Pod以恢复调度功能，命令为：kubectl delete pod -n volcano-system volcano-scheduler-xxxxxxxxx。对于重调度失败的任务Pod，可手动删除原Pod（kubectl delete pod -n <namespace> <pod-name>）或重新下发任务。

