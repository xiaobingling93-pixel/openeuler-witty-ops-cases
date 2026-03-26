# 更换新的NPU模组后，创建虚拟机时NPU模组的TLS使能开关状态不一致

## 内核版本


## 问题现象
更换新的NPU模组后，创建虚拟机时NPU模组的TLS使能开关状态可能存在不一致。

## 问题根因
NPU模组的TLS使能开关默认状态不一致，重新更换NPU模组后，TLS使能开关状态默认关闭。

## 解决方案
执行以下命令重新检查并配置TLS的使能开关状态：
1. 配置TLS使能开关状态：hccn_tool [-i %d] -tls -s [enable %d]
2. 获取TLS使能开关状态：hccn_tool [-i %d] -tls -g
具体操作请参考《Atlas A2 中心推理和训练硬件 HCCN Tool 接口参考》中“使能或关闭TLS”章节。

