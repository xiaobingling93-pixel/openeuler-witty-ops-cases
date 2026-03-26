# 使用Volcano v1.7.0版本，无法查询Pod状态

## 内核版本


## 问题现象
使用Volcano v1.7.0版本时，若当前环境资源不足，执行 kubectl get pod --all-namespaces -o wide 命令查询Pod状态失败。

## 问题根因
当资源不足时，Volcano v1.7.0不会创建Pod，因此无法通过常规命令查询到Pod状态。

## 解决方案
1. 使用 kubectl get pg -A 查询所有PodGroup信息，确认任务对应的PodGroup状态：若STATUS为Inqueue，表示Pod已创建，可正常查询；若为Pending，表示Pod未创建成功。2. 对于Pending状态的PodGroup，执行 kubectl describe pg -n <namespace> <podgroup-name> 查看详细信息，定位具体原因（如queue资源配额不足等）。

