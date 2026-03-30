# ais_bench工具执行动态shape模型推理失败

## 内核版本


## 问题现象
使用ais_bench工具执行动态shape模型推理时失败，报错信息为“Model execute failed”。

## 问题根因
通过开启debug日志分析发现，推理失败的原因是为模型开辟的输出内存空间不足。

## 解决方案
对于动态shape模型，由于输出数据占用的内存大小未知，需在使用ais_bench工具时通过--outputSize参数预估并配置一个合适的输出内存大小。具体参数设置可参考《ais_bench推理工具使用指南》。

