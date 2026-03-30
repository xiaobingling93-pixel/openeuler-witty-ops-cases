# 启动Tengine时提示解析器端口无效的解决方法

## 内核版本


## 问题现象
启动Tengine时提示解析器端口无效，错误信息为“invalid port in resolver \"2017:231::6:6\" in /usr/local/tengine-nginx/conf/nginx.conf:127”。

## 问题根因
此版本Tengine具有自动解析/etc/resolv.conf文件以构造resolver的功能，但该功能暂不支持IPv6，导致在解析IPv6地址时出现端口无效的错误。

## 解决方案
删除“/etc/resolv.conf”文件中的nameserver配置后再次启动Tengine即可解决问题。

