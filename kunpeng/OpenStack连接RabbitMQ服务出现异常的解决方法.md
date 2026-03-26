# OpenStack连接RabbitMQ服务出现异常的解决方法

## 内核版本


## 问题现象
OpenStack部署完成后，提示“ERROR oslo.messaging._drivers.impl_rabbit，Unexpected error occurred serving API: Unable to connect to AMQP server on controller:5672 after inf tries: (0, 0): (541) INTERNAL_ERROR: MessageDeliveryFailure: Unable to connect to AMQP server on controller:5672”。Heat服务也报类似错误。

## 问题根因
RabbitMQ服务异常，可能由SELinux启用、RabbitMQ配置文件中的密码错误或对接IP地址不正确导致。

## 解决方案
1. 关闭SELinux：执行 setenforce 0；
2. 检查并修正当前服务组件的RabbitMQ配置文件中的密码和IP地址；
3. 重启RabbitMQ服务：systemctl restart rabbitmq-server.service；
4. 重启所有报错的OpenStack组件（如Heat）：systemctl restart openstack-heat-api.service openstack-heat-api-cfn.service openstack-heat-engine.service。

