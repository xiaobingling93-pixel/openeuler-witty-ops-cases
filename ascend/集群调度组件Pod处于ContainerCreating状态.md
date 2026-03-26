# 集群调度组件Pod处于ContainerCreating状态

## 内核版本


## 问题现象
部署集群调度组件后，Pod状态长时间处于ContainerCreating。通过kubectl describe命令查看Pod详情，发现事件中报错：MountVolume.SetUp failed for volume "device-ascenddeviceplugin" : hostPath type check failed: /var/log/mindx-dl/ascend-device-plugin is not a directory。

## 问题根因
对应组件的日志目录（如/var/log/mindx-dl/ascend-device-plugin）在宿主机上不存在，导致Kubernetes无法挂载hostPath类型的卷，从而Pod无法正常创建容器。

## 解决方案
1. 在对应节点上创建缺失的日志目录，并设置正确的权限和属主，具体操作参考《MindCluster 集群调度安装指南》中“创建日志目录”章节；2. 手动卸载该组件后重新部署。

