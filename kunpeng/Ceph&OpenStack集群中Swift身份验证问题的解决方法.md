# Ceph&OpenStack集群中Swift身份验证问题的解决方法

## 内核版本


## 问题现象
Swift运行时返回401 Unauthorized错误，提示信息为：Account GET failed: http://ceph1:10001/swift/v1?format=json 401 Unauthorized，响应内容包含{"Code":"AccessDenied","RequestId":"tx000000000000000000002-...}。

## 问题根因
Keystone和Ceph对接身份验证不通过，通常是由于Ceph配置文件中Keystone相关参数设置不正确导致。

## 解决方案
检查ceph1节点中/etc/ceph/ceph.conf文件里Keystone相关的配置是否正确，主要配置项包括：rgw keystone admin user、rgw keystone admin password、rgw keystone admin tenant、rgw keystone admin domain。

