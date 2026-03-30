# 执行PyTorch框架的训练任务时，提示找不到amp_C

## 内核版本


## 问题现象
开启watchdog功能后，下发PyTorch框架的训练任务，报错提示找不到amp_C。

## 问题根因
镜像中找不到megatron_npu路径。

## 解决方案
在train_start.sh中新增环境变量：export PYTHONPATH=$PYTHONPATH:MEGATRON_LM的路径/megatron_npu。

