# ModelArts多机多卡训练GPT2-13B大模型时报错EI0002: The wait execution of the Notify register times out

## 内核版本


## 问题现象
在ModelArts上使用多机多卡训练GPT2-13B大模型时，出现错误EI0002: The wait execution of the Notify register times out。错误信息显示Notify寄存器未在超时时间内收到来自远程rank [1]的Notify记录，相关任务为HcomAllReduce，streamID为153，taskID为19。

## 问题根因
可能的原因包括：各NPU上的训练样本数量不一致；集群中某些NPU执行速度过慢，无法在设定的超时间隔内完成通信操作；或某些NPU在执行过程中发生异常。

## 解决方案
通过设置环境变量HCCL_EXEC_TIMEOUT=7200，延长HCCL通信的超时时间，从而解决该超时错误。

