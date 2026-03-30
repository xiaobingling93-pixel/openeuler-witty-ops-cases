# coredns不断重启的解决方法

## 内核版本


## 问题现象
K8s启动时pod coredns不断重启，处于crashloopbackoff状态。

## 问题根因
具体原因请参考coredns。详见图片：/doc_center/source/zh/kunpengcpfs/ecosystemEnable/Kubernetes/zh-cn_image_0000001217541763.png

## 解决方案
1. 检查“/etc/resolv.conf”是否配置正确。
2. 编辑K8s配置文件：
   kubectl -n kube-system edit configmap coredns
   删除loop字段，保存后删除pod自动重新拉起。

