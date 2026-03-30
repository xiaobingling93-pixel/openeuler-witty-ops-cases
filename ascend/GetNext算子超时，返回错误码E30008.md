# GetNext算子超时，返回错误码E30008

## 内核版本


## 问题现象
执行训练脚本时出现GetNext算子超时，报错信息为：E30008: AI CPU operator execution time out，具体错误节点为aicpu_getnext_IteratorGetNext，伴随rtStreamSynchronizeWithTimeout执行失败，原因为aicpu timeout。

## 问题根因
可能原因包括：1）GetNext算子的预处理阶段耗时过长；2）输入数据集生成不稳定或数据传输网络不稳定，导致Device侧队列入队数量很少（enqueCnt小或lastEnqueTime大）；3）自定义算子逻辑不当（但本例中为标准GetNext算子，故主要考虑前两者）。

## 解决方案
1. 检查训练模型的输入数据集是否正常生成以及数据传输是否稳定；2. 检查Host侧预处理逻辑是否存在性能瓶颈，若确认预处理耗时较大，可通过增大op_execute_timeout配置参数来延长算子超时时间。

