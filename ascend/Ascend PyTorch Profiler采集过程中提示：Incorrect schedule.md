# Ascend PyTorch Profiler采集过程中提示：Incorrect schedule

## 内核版本


## 问题现象
使用Ascend PyTorch Profiler接口采集PyTorch性能数据过程中，打印“Incorrect schedule”提示信息，包括以下几种情况：1）Stop profiler while current state is WARMUP，导致解析数据为空；2）Stop profiler while current state is RECORD，可能导致解析数据不完整；3）Stop profiler while current state is RECORD_AND_SAVE，可能因调度周期未完成而中断。

## 问题根因
问题根因主要有两种情况：1）设置的schedule参数不合理，例如模型训练step总数不足以覆盖skip_first、wait、warmup和active阶段，导致Profiler尚未完成设定的采集周期就提前退出；2）schedule参数repeat设为默认值0，导致最后一个step的数据采集不完整，无法形成有效的性能分析数据。

## 解决方案
检查并合理设置schedule参数，确保训练总step数满足公式：step总数 >= skip_first + (wait + warmup + active) * repeat，以保证Profiler能完整执行warmup、record和save阶段，从而采集到有效的性能数据。

