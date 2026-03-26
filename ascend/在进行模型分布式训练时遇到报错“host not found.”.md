# 在进行模型分布式训练时遇到报错“host not found.”

## 内核版本


## 问题现象
在进行模型分布式训练时，出现报错“ValueError: host not found: Name or service not known”，导致训练进程异常终止。

## 问题根因
分布式训练过程中调用HCCL集合通信模块时，配置的IP地址错误，无法正确解析主机名或服务地址。

## 解决方案
在运行脚本中设置正确的IP地址：单机训练时使用本机IP地址；多机训练时，各节点脚本中的IP应统一设置为master节点的IP地址。

