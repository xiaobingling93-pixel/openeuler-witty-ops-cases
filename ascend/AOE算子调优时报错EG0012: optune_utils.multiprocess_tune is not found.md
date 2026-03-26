# AOE算子调优时报错EG0012: optune_utils.multiprocess_tune is not found

## 内核版本


## 问题现象
在使用AOE进行算子调优（job_type=2）时，系统报错：EG0012: Python module [optune_utils.multiprocess_tune] is not found。

## 问题根因
未安装Python依赖包absl-py，导致无法找到optune_utils.multiprocess_tune模块。

## 解决方案
1. 使用命令 'pip list | grep absl-py' 检查是否已安装absl-py；2. 若未安装，执行 'pip install absl-py' 进行安装。

