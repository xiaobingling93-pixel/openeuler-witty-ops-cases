# 对于报错“No supported Ops kernel and engine are found for [ReduceStdV2A], optype [ReduceStdV2A]”，算子ReduceStdV2A不支持的问题

## 内核版本


## 问题现象
分析迁移工具运行时，出现报错“No supported Ops kernel and engine are found for [ReduceStdV2A], optype [ReduceStdV2A]”。

## 问题根因
当前系统或框架不支持ReduceStdV2A算子。

## 解决方案
可以通过使用std求标准差再平方得到方差（var），均值单独调用mean接口来规避该问题。具体代码修改方式可参考官方提供的示例。

