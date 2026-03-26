# 部署pod一直处于pending状态的解决方法

## 内核版本


## 问题现象
部署Pod一直处于pending状态。

## 问题根因
K8s API server 1.12.2版本的节点label带有beta字段（例如：beta.kubernetes.io/arch=arm64，beta.kubernetes.io/os=linux），与高版本的label不一致，导致调度失败。

## 解决方案
部署yaml前检查nodeSelector标签是否与节点实际label一致，或者通过kubectl describe命令查看Pod pending的具体原因。

