# Containerd作为Kubernetes容器引擎时，集群初始化失败

## 内核版本


## 问题现象
使用Containerd作为Kubernetes容器引擎时，集群初始化失败。

## 问题根因


## 解决方案
参考官方指导初始化Kubernetes集群，根据以下步骤排查安装的软件以及初始化过程是否存在问题：1. 配合参考指导（https://kubernetes.io/zh-cn/docs/setup/production-environment/tools/kubeadm/install-kubeadm/），检查相关软件是否安装，容器运行时是否安装和配置正确；2. 初始化时，是否指定了“--cri-socket”参数，并且配置正确（https://kubernetes.io/zh-cn/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#installing-runtime）；3. 检查是否完成前置条件的处理（https://kubernetes.io/zh-cn/docs/setup/production-environment/container-runtimes/#install-and-configure-prerequisites），cgroup是否配置正确（https://kubernetes.io/zh-cn/docs/setup/production-environment/container-runtimes/#cgroup-drivers）。

