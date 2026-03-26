# 任务容器未成功挂载NPU

## 内核版本


## 问题现象
在任务容器中执行命令 'ls /dev/davinci*' 时系统无回显信息，表明容器内没有成功挂载NPU设备。

## 问题根因
Ascend Device Plugin的启动参数“useAscendDocker”默认为true，表示需要配合Ascend Docker Runtime使用。问题可能由以下原因导致：1）环境未安装Ascend Docker Runtime；2）已安装Ascend Docker Runtime但未重启Docker服务。

## 解决方案
若未安装Ascend Docker Runtime，请参考《MindCluster 集群调度安装指南》安装该工具，然后重启Docker服务，删除旧任务并重新下发任务；若已安装但未重启Docker服务，则只需重启Docker服务，删除旧任务并重新下发任务。可通过命令 'docker info 2>&1 | grep "Default Runtime"' 验证Docker是否使用了Ascend Docker Runtime，预期输出为 'Default Runtime: ascend'。

