# Horizon登录异常的解决方法

## 内核版本


## 问题现象
登录Horizon WebUI时出现异常，执行cat /var/log/httpd/error_log命令提示：RuntimeError: Unable to create a new session key. It is likely that the cache is unavailable.

## 问题根因
无法创建新的session key，原因是cache不可用。

## 解决方案
1. 修改/etc/openstack-dashboard/local_settings配置文件，将SESSION_ENGINE从'django.contrib.sessions.backends.cache'改为'django.contrib.sessions.backends.file'；2. 重启httpd和memcached服务：systemctl restart httpd.service memcached.service。

