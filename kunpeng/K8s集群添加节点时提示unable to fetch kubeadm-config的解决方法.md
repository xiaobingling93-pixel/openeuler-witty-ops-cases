# K8s集群添加节点时提示unable to fetch kubeadm-config的解决方法

## 内核版本


## 问题现象
在向K8s集群添加新节点时，系统提示“unable to fetch kubeadm-config”。

## 问题根因
该问题通常是由于用于加入集群的token错误或已失效导致的。默认情况下，master节点上通过kubeadm生成的token有效期仅为24小时，过期后将无法用于获取kubeadm-config配置。

## 解决方案
1. 登录master节点，执行命令 `kubeadm token list` 检查当前token状态；
2. 若token已失效，则执行 `kubeadm token create` 生成新的临时token；
3. 使用新生成的token重新执行节点加入命令即可成功添加节点。

