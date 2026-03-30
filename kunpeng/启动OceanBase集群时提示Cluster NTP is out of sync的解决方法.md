# 启动OceanBase集群时提示Cluster NTP is out of sync的解决方法

## 内核版本


## 问题现象
启动OceanBase集群时提示：[ERROR] Cluster NTP is out of sync.

## 问题根因
OceanBase集群中主机之间的时差超过100ms，导致集群无法正常启动。

## 解决方案
1. 关闭防火墙：systemctl stop firewalld、systemctl disable firewalld。
2. 在所有集群节点和NTP客户端安装NTP服务：yum -y install ntp ntpdate。
3. 备份原有NTP配置：cd /etc && mv ntp.conf ntp.conf.bak。
4. 选择一台服务器（如192.168.0.216）作为NTP服务端，配置/etc/ntp.conf如下：
   restrict 127.0.0.1
   restrict ::1
   restrict 192.168.0.216 mask 255.255.255.0
   server 127.127.1.0
   fudge 127.127.1.0 stratum 8
5. 在其他客户端节点配置/etc/ntp.conf，添加：server 192.168.0.216。
6. 启动NTP服务端：systemctl start ntpd、systemctl enable ntpd。
7. 客户端强制同步时间：ntpdate 192.168.0.216。
8. 将系统时间写入硬件时钟：hwclock -w。
9. 配置定时任务自动同步时间：安装crontab，编辑crontab文件加入 */10 * * * * /usr/sbin/ntpdate 192.168.0.216。

