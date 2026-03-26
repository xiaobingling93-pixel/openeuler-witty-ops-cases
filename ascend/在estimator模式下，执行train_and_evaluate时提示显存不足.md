# 在estimator模式下，执行train_and_evaluate时提示显存不足

## 内核版本


## 问题现象
在estimator模式下，执行train_and_evaluate时报错，提示显存不足：Sum of total mem_offset:26496001536 and var_mem_size:11776003072 is greater than memory manager malloc max size 33285996544。

## 问题根因
在train_and_evaluate模式下，若未启用动态扩容会两次建表，如果表特别大的话可能会导致显存不足。

## 解决方案
可以改成扩容模式进行规避，扩容模式只会建一次表；或者减小batch size。

