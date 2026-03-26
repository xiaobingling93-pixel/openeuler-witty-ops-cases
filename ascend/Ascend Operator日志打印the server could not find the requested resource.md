# Ascend Operator日志打印the server could not find the requested resource

## 内核版本


## 问题现象
Ascend Operator日志中反复出现错误信息：'the server could not find the requested resource (get jobs.batch.volcano.sh)'，具体表现为无法watch或list *v1alpha1.Job资源。

## 问题根因
未安装Volcano组件，导致Ascend Operator无法找到所需的Kubernetes自定义资源jobs.batch.volcano.sh。

## 解决方案
安装Volcano组件后，该错误将自动解决，日志不再打印相关错误内容。

