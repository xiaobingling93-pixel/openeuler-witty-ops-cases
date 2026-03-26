# 组件启动yaml执行成功，找不到组件对应的Pod

## 内核版本


## 问题现象
执行Ascend Device Plugin的YAML文件后显示创建成功，Kubernetes DaemonSet资源已存在，但对应Pod未被调度或无法找到。

## 问题根因
目标节点缺少Ascend Device Plugin所需的标签“accelerator=huawei-Ascendxxx”（如accelerator=huawei-Ascend910），导致Pod无法被正确调度到该节点。

## 解决方案
使用命令“kubectl label nodes 主机名称 accelerator=huawei-Ascend910”为对应节点添加正确的标签，具体标签值可参考《MindCluster 集群调度安装指南》中关于创建节点标签的章节。

