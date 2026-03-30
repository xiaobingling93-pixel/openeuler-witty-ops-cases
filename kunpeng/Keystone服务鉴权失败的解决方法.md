# Keystone服务鉴权失败的解决方法

## 内核版本


## 问题现象
在Nova执行命令openstack compute service list查看service list时提示“The server is currently unavailable. The Keystone service is temporarily unavailable.”。

## 问题根因
nova密码不正确。

## 解决方案
1. 重新配置nova密码：openstack user set --password NEW_PASSWORD USERNAME；2. 检查配置文件“/etc/nova/nova.conf”的[keystone_authtoken]字段内容，并修改为正确的信息；3. 重启服务，使修改后的配置生效：systemctl restart openstack-nova-api.service openstack-nova-scheduler.service openstack-nova-conductor.service。

