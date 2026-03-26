# 模型运行时出现coredump，报错terminate called after throwing an instance of ‘std::runtime_error’

## 内核版本


## 问题现象
模型在运行过程中发生coredump，终端报错信息为：terminate called after throwing an instance of ‘std::runtime_error’。

## 问题根因
当前算子采用异步下发机制，当算子执行出错时会抛出异常，导致主线程崩溃并产生coredump。

## 解决方案
通过设置环境变量 ASCEND_LAUNCH_BLOCKING=1（即执行 export ASCEND_LAUNCH_BLOCKING=1），使算子同步执行。再次运行模型后，可在报错时获取具体的调用栈信息，从而进一步定位和分析问题。

