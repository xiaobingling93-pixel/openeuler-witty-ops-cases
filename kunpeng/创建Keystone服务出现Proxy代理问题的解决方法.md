# 创建Keystone服务出现Proxy代理问题的解决方法

## 内核版本


## 问题现象
使用openstack命令创建Keystone服务时，出现“ProxyError”问题，提示“Caused by ProxyError(‘Cannot connect to proxy.’, error(104, ’Connection reset by peer’))”。

## 问题根因
由于配置了Proxy代理，但是openstack命令使用的是http的方式传递，与配置的代理有冲突。

## 解决方案
关闭proxy代理，执行命令：unset ftp_proxy http_proxy https_proxy。

