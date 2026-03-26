# 应用在Docker容器中运行失败的解决方法

## 内核版本


## 问题现象
进行兼容性测试时，若应用在Docker容器中运行，会出现报错信息（如图1所示）。

## 问题根因
compatibility_testing.sh文件中的检测命令没有对Docker容器环境做对应适配。

## 解决方案
需要对“compatibility_testing/Chinese”路径下的compatibility_testing.conf、compatibility_testing.sh文件进行修改：1. 将compatibility_testing.conf文件中的“kubernetes_env=”内容修改为“kubernetes_env=Y”；2. 在compatibility_testing.sh文件中，将check_process()函数中第二次出现的“kubectl get all --all-namespaces”内容修改为“docker ps”。

