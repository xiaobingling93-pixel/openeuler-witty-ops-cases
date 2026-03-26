# AI Core算子执行时间超时导致网络运行失败

## 内核版本


## 问题现象
执行模型推理时，返回模型执行失败。Device侧日志中出现ERROR级别的打印日志：[ERROR] TSCH(-1,null):... bs_done_exception_proc_timeout: slot_id=1,TS_ctrl=0x4,exception_core_list=0x0,current core usage=0x1,AI_CORES_COUNT=2, fault_task=0。

## 问题根因
AI Core中算子执行task时间超过系统设定的超时限制。昇腾310 AI处理器的超时时间为55秒，昇腾910 AI处理器的超时时间为68秒。

## 解决方案
1. 查看Device侧日志，通过关键字“bs_done_exception_proc_timeout”定位fault_task ID；2. 在Host侧日志中根据该task ID搜索“TaskLaunched”和“task_id=<ID>”，找到对应的kernel_name，从而确定超时算子名称；3. 参考《算子开发指南》中TIK性能优化章节对算子进行优化。

