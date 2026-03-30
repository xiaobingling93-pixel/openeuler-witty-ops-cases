# Swift服务运行提示Errno 13的解决方法

## 内核版本


## 问题现象
安装验证过程中，Swift组件中“openstack-swift-object-replicator.service”服务和“openstack-swift-object-updater.service”服务运行时提示“ERROR: Unable to access /srv/node/sdb: [Errno 13] Permission denied: '/srv/node/sdb'”。

## 问题根因
无法访问对象存储盘，在其他配置均正确的情况下，一般为SELinux安全上下文或文件夹权限的问题。

## 解决方案
1. 进入存储节点，执行以下命令确保“/srv”目录中的所有文件都定义了正确的SELinux安全上下文：
   sudo chown -R swift:swift /srv/node/
   sudo restorecon -R /srv
2. 重新启动Swift服务：
   sudo service openstack-swift-account start
   sudo service openstack-swift-container start
   sudo service openstack-swift-object start
   sudo chkconfig openstack-swift-account on
   sudo chkconfig openstack-swift-container on
   sudo chkconfig openstack-swift-object on
3. 重启并关闭防火墙：
   systemctl restart firewalld.service
   systemctl stop firewalld.service
4. 检查Swift组件服务状态，确认所有服务正常运行。

