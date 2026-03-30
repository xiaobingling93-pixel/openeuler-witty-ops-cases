# 服务器重启后K8s重启失败

## 内核版本


## 问题现象
服务器重启后Kubernetes（K8s）无法正常启动，执行kubectl get pod命令时提示连接被拒绝：'The connection to the server xxx.xxx.xxx.xxx:6443 was refused - did you specify the right host or port?'。同时通过free -m命令发现系统Swap未关闭，Swap空间总量为38146MB。

## 问题根因
Kubernetes要求在运行环境中必须关闭Swap，而服务器重启后Swap自动启用，导致K8s组件无法正常启动。

## 解决方案
临时解决方案：执行swapoff -a命令关闭Swap，等待K8s自动恢复。永久解决方案：创建脚本/usr/local/scripts/dls_swap_check.sh，在系统启动时自动检测并关闭Swap，并将该脚本添加到/etc/rc.local中确保开机执行。脚本内容包含循环检查Swap状态并在非零时调用swapoff -a，同时设置适当权限（chmod 750）。

