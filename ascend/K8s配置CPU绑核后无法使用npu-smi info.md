# K8s配置CPU绑核后无法使用npu-smi info

## 内核版本


## 问题现象
在Atlas 800 推理服务器（型号 3000）（Arm），操作系统CentOS 7.6上，使用K8s（版本1.12）进行NPU相关业务调度。配置K8s的参数 --kube-reserved=cpu=2,memory=250Mi --cpu-manager-policy=static --feature-gates=CPUManager=true 开启CPU绑核后，执行 npu-smi info 命令报错。

## 问题根因
K8s启用static CPU管理策略后，会通过reconcile机制动态更新容器的CPU set。Ascend Docker Runtime在挂载昇腾驱动库和设备信息时未将相关信息同步给Docker Engine。当RunC在update过程中调用device Set方法并根据cgroup config调整设备文件时，导致原先挂载时添加的cgroup设备访问权限丢失，从而使得npu-smi info无法正常访问NPU设备。

## 解决方案
使用Ascend Device Plugin插件替代Ascend Docker Runtime进行设备挂载。具体操作为修改Ascend Device Plugin的驱动参数“-useAscendDocker=false”，然后重新安装Ascend Device Plugin，以确保cgroup设备访问权限在K8s CPU绑核场景下不会丢失。

