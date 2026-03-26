# 断点续训任务被重调度后Pod状态不一致

## 内核版本


## 问题现象
在多节点集群环境中下发分布式训练任务，若环境资源刚好满足且开启任务重调度（参数fault-scheduling为grace），当发生故障触发重调度后，概率性出现一个Pod状态为Running、另一个Pod状态为Pending的情况；即使后续故障恢复，Pending状态的Pod仍无法恢复。

## 问题根因
开源代码中对任务数量的判断存在缺陷：当Pod被终止时，若容器脚本返回0（表示成功），K8s会将Pod状态标记为Success，Volcano调度器误认为该Pod已成功重启并计入gang调度条件，导致部分Pod提前创建；当原Pod真正终止并尝试重新拉起时，因资源不足而卡在Pending状态。此外，未使用断点续训脚本及集群资源不足也是诱因。

## 解决方案
手动删除已运行的Pod（kubectl delete pod -n <namespace> <pod名称>），或直接删除整个任务后重新下发。

