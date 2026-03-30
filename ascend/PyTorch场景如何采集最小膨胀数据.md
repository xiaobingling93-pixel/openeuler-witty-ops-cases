# PyTorch场景如何采集最小膨胀数据

## 内核版本


## 问题现象
模型运行过程中开启Profiling采集性能数据会造成性能膨胀，具体表现是开启Profiling后模型性能数据采集step打屏耗时较不开启Profiling耗时变长，两者差值为膨胀时间。

## 问题根因
膨胀程度与Profiling采集设置相关，主要影响因素包括：1. with_stack开关（开启会获取调用栈信息，性能影响巨大）；2. profiler_level（级别越高，采集数据量越大，性能膨胀越严重）；3. activities设置（采集的事件类型）；4. 其他采集开关。

## 解决方案
推荐使用最小膨胀配置进行性能数据采集，特别是在与GPU性能对比时。最小膨胀配置示例：仅采集NPU活动（activities=[torch_npu.profiler.ProfilerActivity.NPU]），设置schedule(wait=1, warmup=1, active=1, repeat=1, skip_first=20)，并使用tensorboard_trace_handler保存结果。若需一般性能分析，可采用包含CPU和NPU活动、profiler_level设为Level1等的推荐配置。

