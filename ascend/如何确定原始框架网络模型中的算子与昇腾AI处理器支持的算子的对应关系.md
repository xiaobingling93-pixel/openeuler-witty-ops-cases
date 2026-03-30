# 如何确定原始框架网络模型中的算子与昇腾AI处理器支持的算子的对应关系

## 内核版本


## 问题现象
用户在使用精度比对工具或性能比对工具进行算子分析时，若发现某些算子存在精度或性能问题，需通过ATC工具参数（如--modify_mixlist）调整算子计算精度，但不清楚如何获取这些算子在昇腾AI处理器中对应的Ascend IR OpType。

## 问题根因
用户不了解如何将原始框架网络模型中的算子映射到昇腾AI处理器所支持的Ascend IR算子类型（OpType），导致无法正确配置ATC工具参数进行模型优化。

## 解决方案
可通过以下方式获取Ascend IR算子OpType：1）使用Profiling工具时，导出op_summary_*.csv文件，其中“OP Type”列即为昇腾AI处理器支持的算子OpType；2）使用精度比对工具时，从result_*.csv文件的“NPUDump”列找到问题算子名，并在对应dump数据文件开头检索到对应的OpType。

