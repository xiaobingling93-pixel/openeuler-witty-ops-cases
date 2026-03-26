# 网络调测时ReduceSum算子性能差如何处理

## 内核版本


## 问题现象
网络调测时整体性能较慢，通过Profiling工具分析发现ReduceSum算子性能很差，其输入数据类型为DT_FLOAT16，且block_dim字段值为1，表明未开启多核并行计算。

## 问题根因
在昇腾AI处理器上，当ReduceSum算子的输入数据类型为float16时，由于硬件限制，在某些场景下无法开启多核并行计算，导致性能下降。

## 解决方案
针对ReduceSum算子性能差的问题，可采取以下两种措施：1）若网络未开启混合精度，可在ReduceSum前插入Cast算子，将输入从float16转为float32，以启用多核并发；2）若已开启混合精度，可将ReduceSum加入混合精度黑名单（如配置ops_info.json中的black-list），防止其被自动转换为float16，从而避免性能劣化。

