# 开启watchdog模型运行时出现coredump，报错terminate called after throwing an instance of ‘std::runtime_error’

## 内核版本


## 问题现象
开启watchdog模型运行时报错terminate called after throwing an instance of ‘std::runtime_error’，导致程序coredump。

## 问题根因
开启watchdog子线程后，watchdog检测到异常并抛出异常，进而导致主线程coredump。

## 解决方案
根据watchdog抛出的异常信息和plog日志分析问题的根本原因，并针对性地修复。

