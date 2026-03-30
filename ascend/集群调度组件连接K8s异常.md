# 集群调度组件连接K8s异常

## 内核版本


## 问题现象
集群调度组件连接K8s异常。

## 问题根因
节点B在K8s集群中导入过KubeConfig文件，当节点B加入一个新的K8s集群之后，启动组件会默认使用之前导入的KubeConfig文件。

## 解决方案
如果组件使用ServiceAccount方式启动，根据《MindCluster 集群调度安装指南》的“安装部署 > 手动安装 > Resilience Controller >（可选）导入证书和KubeConfig”章节的集群调度组件证书配置文件表，找到组件对应的KubeConfig文件删除后，再删除对应的Pod即可恢复；如果组件使用KubeConfig文件方式启动，重新导入新的KubeConfig文件后，再删除对应的Pod即可恢复。

