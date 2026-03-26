# Profiling出现format为NHWC的算子性能较低

## 内核版本


## 问题现象
Profiling数据中出现format为NHWC的算子，且性能较低。

## 问题根因
NPU主要支持format为NCHW的算子，当format为NHWC时会导致性能下降。

## 解决方案
修改算子的format为NCHW以提升性能。

