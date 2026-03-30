# 执行openstack network agent list时提示HttpException :503的解决方法

## 内核版本


## 问题现象
执行命令 openstack network agent list 时提示“HttpException :503”。

## 问题根因
neutron密码不正确。

## 解决方案
1. 重新配置neutron密码：openstack user set --password NEW_PASSWORD USERNAME；2. 检查配置文件“/etc/neutron/neutron.conf”的[keystone_authtoken]字段内容，并修改为正确的信息；3. 重启服务使配置生效：systemctl restart neutron-server.service。

