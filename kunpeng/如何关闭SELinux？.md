# 如何关闭SELinux？

## 内核版本


## 问题现象
用户需要关闭SELinux，但不清楚具体操作方法。

## 问题根因


## 解决方案
临时关闭SELinux：执行命令 setenforce 0；永久关闭SELinux：执行命令 sed -i "s/SELINUX=enforcing/SELINUX=disabled/g" /etc/selinux/config（需重启服务器生效）。

