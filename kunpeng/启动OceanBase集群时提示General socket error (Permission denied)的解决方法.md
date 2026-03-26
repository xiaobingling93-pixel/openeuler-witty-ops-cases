# 启动OceanBase集群时提示General socket error (Permission denied)的解决方法

## 内核版本


## 问题现象
部署HAProxy服务过程中，无法连接HAProxy服务。查看HAProxy状态时提示：General socket error (Permission denied)。

## 问题根因
HAProxy不允许被连接到其他端口，这是由于SELinux策略限制了HAProxy进程的网络连接权限。

## 解决方案
执行如下命令，允许HAProxy进程建立到任何地址和端口的连接：
```
getsebool haproxy_connect_any
setsebool -P haproxy_connect_any 1
```

