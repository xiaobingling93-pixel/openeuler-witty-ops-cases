# MindSpore报错Framework ERROR: Init hccl graph adapter failed

## 内核版本


## 问题现象
MindSpore运行分布式模型时报错：RuntimeError: Ascend collective communication initialization failed. Framework Error Message: Init hccl graph adapter failed.

## 问题根因
fwkacllib加载失败，导致CANN HCCL相关组件初始化异常。

## 解决方案
1. 使用CANN包的环境变量配置脚本：source set_env.sh；2. 或手动添加环境变量：export LD_LIBRARY_PATH=fwkacllib/lib64:$LD_LIBRARY_PATH。

