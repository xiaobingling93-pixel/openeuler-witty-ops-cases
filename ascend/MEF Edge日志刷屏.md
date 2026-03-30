# MEF Edge日志刷屏

## 内核版本


## 问题现象
MEF Edge成功对接cloudcore后，edge_main产生大量消息，造成日志刷屏，日志内容为：edgecore proxy receive msg router: {Source: Destination:EdgeCore Option:query Resource:default/node/***}, route: {Source:edge_main Group:resource Operation:response Resource:default/node/***}。

## 问题根因
kube-controller-manager未对节点分配CIDR，而edgecore会持续查询节点状态，直到CIDR被分配为止。

## 解决方案
登录安装MEF Center的主机，修改kube-controller-manager配置文件（通常位于/etc/kubernetes/manifests/kube-controller-manager.yaml），添加启动参数：--cluster-cidr=192.168.0.0/16 和 --allocate-node-cidrs=true。

