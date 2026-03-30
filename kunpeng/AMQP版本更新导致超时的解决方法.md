# AMQP版本更新导致超时的解决方法

## 内核版本


## 问题现象
采用AMQP 5.0.5版本时出现超时问题，错误提示为“Failed reporting state!: oslo_messaging.exceptions.MessagingTimeout: Timed out waiting for a reply to message ID...”。

## 问题根因
AMQP 5.0.5版本存在缺陷，导致消息通信超时。

## 解决方案
1. 卸载当前AMQP组件并安装5.0.8版本：
   pip3 uninstall amqp
   pip3 install amqp==5.0.8 --target=/usr/lib/python3.7/site-packages
2. 重启相关服务：
   systemctl restart httpd.service memcached.service rabbitmq-server.service mariadb.service neutron-server

