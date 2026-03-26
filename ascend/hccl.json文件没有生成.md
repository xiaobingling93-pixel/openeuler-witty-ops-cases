# hccl.json文件没有生成

## 内核版本


## 问题现象
当启动一个训练任务后，训练任务容器内部的hccl.json文件一直处于initializing状态（默认路径：/user/serverid/devindex/config/hccl.json）。

## 问题根因
可能的原因包括：1. Ascend Operator没有正常启动；2. Ascend Device Plugin启动参数配置了“-volcanoType=false”；3. Ascend Device Plugin未正确获取到device ip，导致无法写入Pod的Annotations，日志中出现“Get device ip failed”。

## 解决方案
针对原因一：参考《MindCluster 集群调度安装指南》重新安装Ascend Operator；针对原因二：修改Ascend Device Plugin的启动参数为“-volcanoType=true”并重新apply对应的yaml文件；针对原因三：按照《MindCluster Ascend Deployer用户指南》使用HCCN Tool工具正确配置device ip。

