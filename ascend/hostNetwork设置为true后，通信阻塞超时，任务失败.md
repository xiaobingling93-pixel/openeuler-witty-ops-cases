# hostNetwork设置为true后，通信阻塞超时，任务失败

## 内核版本


## 问题现象
训练任务开启hostNetwork为true后，出现通信阻塞超时，导致任务失败。

## 问题根因
hostNetwork设置为true后，未在任务yaml中配置环境变量参数HCCL_IF_IP，导致HCCL无法确认与哪个网卡IP建立通信，从而引发通信超时。

## 解决方案
在任务yaml中设置hostNetwork为true的同时，需同步配置环境变量HCCL_IF_IP为status.hostIP，以指定root通信网卡IP为hostIP，使HCCL成功建链，解决通信超时问题。

