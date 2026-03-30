# DockerHub网络可达，但下拉镜像超时的解决方法

## 内核版本


## 问题现象
DockerHub网络可达，但从DockerHub拉取镜像时出现超时。

## 问题根因
docker pull被SELinux拒绝访问。

## 解决方案
1. 临时关闭SELinux：执行命令 setenforce 0。
2. 永久修改SELinux配置：编辑“/etc/selinux/config”文件，将SELINUX=enforcing改为SELINUX=permissive或disabled。

