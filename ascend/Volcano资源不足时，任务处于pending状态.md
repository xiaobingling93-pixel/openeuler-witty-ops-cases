# Volcano资源不足时，任务处于pending状态

## 内核版本


## 问题现象
使用Volcano进行任务调度时，若申请的资源大于当前环境可用资源，任务不会被调度，状态会置为pending；若申请的资源超过集群资源上限（例如在仅有8个NPU的集群中申请16个NPU），任务将一直处于pending状态。

## 问题根因
申请的资源超过集群当前可用资源或总资源上限，导致volcano-scheduler无法调度任务，且未自动终止该任务。

## 解决方案
1. 在提交任务前确保集群资源充足；2. 若任务已处于pending状态，可通过kubectl get vcjob -n <namespace> 查找任务；3. 使用 kubectl delete vcjob <job-name> -n <namespace> 删除无法调度的任务。

