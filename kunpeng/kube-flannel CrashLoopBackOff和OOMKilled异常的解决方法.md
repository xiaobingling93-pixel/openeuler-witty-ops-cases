# kube-flannel CrashLoopBackOff和OOMKilled异常的解决方法

## 内核版本


## 问题现象
kubectl get pod -n kube-system发现网络插件kube-flannel一直在尝试重启，有时能够正常，有时提示“CrashLoopBackOff”，有时提示“OOMKilled”。

## 问题根因
kube-flannel.yml文件中的内存配置不足。

## 解决方案
1. 修改kube-flannel.yml中内存配置，将其调大一些。比如将内存从50M修改到200M。
2. 重新apply：kubectl apply -f kube-flannel.yml

