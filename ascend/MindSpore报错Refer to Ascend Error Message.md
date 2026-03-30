# MindSpore报错Refer to Ascend Error Message

## 内核版本


## 问题现象
MindSpore运行时报通用性错误：RuntimeError: Run task for graph:kernel_graph_x error! The details refer to 'Ascend Error Message'，错误信息无实质性内容。

## 问题根因
该错误是MindSpore拦截CANN底层错误后抛出的通用性错误。实际根因为环境配置不配套，具体表现为AICPU模块加载失败（module_type=E39999, msg: open so failed），即未使用与当前环境匹配的CANN软件版本。

## 解决方案
1. 设置环境变量以获取详细错误信息：export ASCEND_GLOBAL_LOG_LEVEL=1 和 export ASCEND_SLOG_PRINT_TO_STDOUT=1；2. 重新运行程序，根据日志中的ERROR信息定位具体错误码和原因；3. 确认并使用与硬件和驱动配套的CANN及MindSpore软件版本；4. 若非环境问题，可根据错误码查阅CANN手册或联系华为工程师协同解决。

