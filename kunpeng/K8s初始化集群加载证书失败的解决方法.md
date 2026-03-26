# K8s初始化集群加载证书失败的解决方法

## 内核版本


## 问题现象
初始化集群时提示“failed to load certificate: couldn't load the certificate file /etc/kubernetes/pki/apiserver.crt: open /etc/kubernetes/pki/apiserver.crt: no such file or directory”。

## 问题根因
apiserver.crt由kubeadm组件自动生成，该问题是因为环境中的残余配置文件没有清理。

## 解决方案
删除“$HOME/.kube/config”文件并执行kubeadm reset命令方可解除。

