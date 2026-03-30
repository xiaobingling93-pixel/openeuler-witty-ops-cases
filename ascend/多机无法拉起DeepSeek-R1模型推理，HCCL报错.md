# 多机无法拉起DeepSeek-R1模型推理，HCCL报错

## 内核版本


## 问题现象
在多节点启动DeepSeek-R1模型推理服务时，出现HCCL通信错误，具体表现为开启算子库和ATB日志后报HCCL相关错误。

## 问题根因
每台机器NPU底层TLS校验行为不一致，导致HCCL通信失败。

## 解决方案
检查所有节点的NPU设备TLS开关状态是否一致，使用命令 'for i in {0..7}; do hccn_tool -i $i -tls -g ; done | grep switch' 查看状态；若不一致，统一设置为0或1，对应命令分别为：'for i in {0..7};do hccn_tool -i $i -tls -s enable 0;done' 或 'for i in {0..7};do hccn_tool -i $i -tls -s enable 1;done'。

