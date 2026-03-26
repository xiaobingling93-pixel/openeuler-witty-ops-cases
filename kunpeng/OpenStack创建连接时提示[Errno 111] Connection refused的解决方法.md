# OpenStack创建连接时提示[Errno 111] Connection refused的解决方法

## 内核版本


## 问题现象
执行 openstack network agent list 命令时，提示无法建立到 http://controller:9696/v2.0/agents 的连接，错误信息为：[Errno 111] Connection refused。

## 问题根因
neutron-server配置错误导致服务异常，具体可能与 /etc/neutron/neutron.conf 文件中 [database] 部分的 connection 配置不正确有关。

## 解决方案
1. 检查 /etc/neutron/neutron.conf 文件中 [database] 的 connection 配置是否正确；2. 重启 Neutron 相关服务，例如执行 systemctl restart neutron-server.service。

