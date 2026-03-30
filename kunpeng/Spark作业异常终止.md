# Spark作业异常终止

## 内核版本


## 问题现象
Spark作业异常终止，日志中出现错误信息：'<KunpengAlgorithmLibrary> ERROR: The software cannot run normally, please confirm the processor model.'

## 问题根因
算法加速库仅支持鲲鹏体系架构，在非鲲鹏体系架构的机器上运行会导致该错误。

## 解决方案
请检查运行环境是否为鲲鹏处理器环境，确保算法加速库仅在鲲鹏处理器的服务器中运行。

