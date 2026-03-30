# 提交Yarn任务时，清除之前运行的Yarn任务的解决方法

## 内核版本


## 问题现象
基于Hadoop的任务测试执行过程中，Yarn Web界面存在之前运行的Yarn任务。

## 问题根因
存留的yarn任务没有退出。

## 解决方案
1. 结束测试，查看Yarn任务，使用命令：yarn app -list 列出任务，然后使用 yarn app -kill applicationID 杀掉对应任务。2. 重新开始测试。

