# 执行kubectl get nodes时提示The connection to the server localhost的解决方法

## 内核版本


## 问题现象
执行kubectl get nodes时，提示“The connection to the server localhost:8080 was refused”。

## 问题根因
Kube的config文件并没有赋予合理所属权导致执行权限不够。

## 解决方案
1. 依次执行以下命令重新赋予合理所属权：
cp /etc/kubernetes/admin.conf $HOME/
chown $(id -u):$(id -g) $HOME/admin.conf
2. 执行如下命令更新环境变量：
export KUBECONFIG=$HOME/admin.conf
3. 重新执行kubectl get nodes查看节点。

