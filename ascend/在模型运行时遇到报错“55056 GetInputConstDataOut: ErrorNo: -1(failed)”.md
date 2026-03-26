# 在模型运行时遇到报错“55056 GetInputConstDataOut: ErrorNo: -1(failed)”

## 内核版本


## 问题现象
在模型训练过程中，日志中反复出现错误信息：“55056 GetInputConstDataOut: ErrorNo: -1(failed) [COMP] [DEFAULT][Get][InputImpl] failed, dst_name:perm”。

## 问题根因
该报错是由于模型训练过程中调用了某个公共API接口所导致。

## 解决方案
该报错信息不影响模型训练的功能与性能，可以安全忽略。

