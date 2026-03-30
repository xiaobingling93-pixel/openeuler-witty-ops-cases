# 执行openstack network list命令时提示Internal Server Error, HTTP 500的解决方法

## 内核版本


## 问题现象
执行openstack network list命令时返回HTTP 500错误，日志/var/log/neutron/server.log中显示数据库连接错误：oslo_messaging.rpc.server OperationalError: (pymysql.err.OperationalError) (1040, u'Too many connections')。

## 问题根因
OpenStack持续调度导致数据库连接数达到上限，原因是MariaDB配置的max_connections值过小，无法满足当前并发需求。

## 解决方案
1. 修改MariaDB配置文件/etc/my.cnf.d/openstack.cnf，在[mysqld]下设置max_connections = 4096；2. 调整系统最大文件打开数：在/etc/security/limits.conf中添加'* soft nofile 65536'和'* hard nofile 65536'，并在/etc/pam.d/login中添加'session required /lib/security/pam_limits.so'，执行ulimit -SHn 65536；3. 在/etc/sysctl.conf中设置fs.file-max = 65536并执行sysctl -p生效；4. 修改/usr/lib/systemd/system/mariadb.service，在[Service]下添加LimitNOFILE=65535和LimitNPROC=65535，然后执行systemctl daemon-reload并重启mariadb.service；5. 重启所有OpenStack相关服务，包括Neutron、Nova、Glance和Cinder。

