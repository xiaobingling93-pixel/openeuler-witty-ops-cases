# 组件Pod状态不为Running

## 内核版本


## 问题现象
部署集群调度组件后，通过命令kubectl get pods --all-namespaces -o wide查看各组件状态，发现组件的Pod状态不为Running。

## 问题根因
可能的原因包括：1）Pod状态为ImagePullBackOff或ErrImagePull，由镜像版本不正确导致；2）Pod状态为CrashLoopBackOff或Error，由镜像架构错误或日志路径无权限引起；3）Pod状态为Pending，因管理节点未配置selector。

## 解决方案
针对镜像问题，检查并重新准备正确版本的镜像；针对镜像架构错误，重新准备匹配架构的镜像；针对日志路径权限问题，按照安装指南创建日志目录并设置正确权限和属主；针对Pending状态，为管理节点配置相应的selector。

