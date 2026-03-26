# Spark执行INSERT语句查询多个大宽表Join时，SMJ算子出现内存不足导致core dump问题的解决方法

## 内核版本


## 问题现象
在Spark执行INSERT语句且只有1个数据分区的场景下，当出现50个表连续SMJ（Sort Merge Join）操作时，可能会导致SMJ算子在堆外内存耗尽时调用new来申请vector内存，从而引发core dump问题。

## 问题根因
算子加速采用列式处理，相比Spark开源版本的行式处理内存占用更大，且SMJ算子计算过程中申请的资源需在Task结束后才能释放。在INSERT语句且只有1个数据分区的情况下，Spark仅生成1个task执行全部50个表的Sort Merge Join，导致38g堆外内存耗尽，再次通过new申请内存时发生core dump。

## 解决方案
该场景属于极端情况，正常业务应避免单task执行大量表Join。若触发该问题，可采取以下措施规避：1. 调整spark.memory.offHeap.size参数增大堆外内存后重新运行任务；2. 回退到Spark开源版本流程执行任务。

