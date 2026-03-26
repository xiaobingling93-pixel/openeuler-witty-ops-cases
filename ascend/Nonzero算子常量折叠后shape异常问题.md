# Nonzero算子常量折叠后shape异常问题

## 内核版本


## 问题现象
使用atc工具将onnx模型转换为om模型后，通过msame工具进行推理时出现错误。具体表现为PartitionedCall_NonZero_14_Transpose_219节点的输入shape为[-1,1]，而正常情况下常量折叠后的shape不应包含负数。

## 问题根因
Nonzero算子属于infershape依赖tensor值的三类算子，在常量折叠场景下，其shape在infershape阶段被刷新为-1，但缺少后续compute完成后将实际shape反刷回的流程，导致GE引擎获取到的shape为[1,-1]。

## 解决方案
修改算子信息库配置文件/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/aicpu/aicpu_kernel/config/aicpu_kernel.json，在Nonzero算子配置中添加opInfo.opsFlag=OPS_FLAG_CLOSE，以禁用该算子的常量折叠功能。

