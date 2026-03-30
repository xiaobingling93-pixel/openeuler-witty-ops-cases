# 在模型运行时遇到报错“terminate called after throwing an instance of 'c10::Error' what(): HelpACLExecute:”

## 内核版本


## 问题现象
模型运行时报错：terminate called after throwing an instance of 'c10::Error' what(): HelpACLExecute: ***/pytorch/c10/npu/NPUStream.cpp:158，错误发生在Task任务下发阶段，终端仅显示封装后的异常信息，无法直接定位具体错误原因。

## 问题根因
由于开启了Task多线程下发，上层对原始错误进行了封装，导致HelpACLExecute报错信息中缺失详细的错误上下文，无法直接从终端输出中获取根本原因。

## 解决方案
可通过两种方式解决：1）查看主机日志文件（默认路径为/var/log/npu/slog/host-0/），按时间查找host-0前缀的日志，搜索“ERROR”获取详细错误信息；2）关闭多线程下发，设置环境变量 export ASCEND_LAUNCH_BLOCKING=1 后重新运行代码，此时终端会输出更明确的错误信息以便定位问题。

