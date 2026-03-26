# 使用glibc 2.28版本运行业务调用malloc接口出现Core Dump问题

## 内核版本


## 问题现象
在glibc 2.28版本的docker环境中运行视频解析、目标识别相关业务时出现Core Dump，堆栈信息显示异常发生在调用glibc的malloc接口时。

## 问题根因
glibc 2.28版本存在bug，导致malloc接口在特定条件下触发异常。

## 解决方案
通过设置环境变量禁用tcache机制：export GLIBC_TUNABLES=glibc.malloc.tcache_count=0。该问题已在glibc 2.29版本中修复。

