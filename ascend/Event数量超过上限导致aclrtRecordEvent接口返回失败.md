# Event数量超过上限导致aclrtRecordEvent接口返回失败

## 内核版本


## 问题现象
调用aclrtRecordEvent接口在Stream中记录一个Event时，接口返回失败，日志显示Event ID申请失败，错误码为7，Event ID为-1。

## 问题根因
Event ID的数量超过系统上限，通常发生在多Stream同步等待场景下频繁申请Event资源但未及时释放。

## 解决方案
在调用aclrtRecordEvent和aclrtStreamWaitEvent接口后，若指定的Event已完成，应及时调用aclrtResetEvent接口释放Event资源，避免Event数量超出上限。

