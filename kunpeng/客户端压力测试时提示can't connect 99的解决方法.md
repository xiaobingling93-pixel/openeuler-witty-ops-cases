# 客户端压力测试时提示can't connect 99的解决方法

## 内核版本


## 问题现象
客户端在进行压力测试时提示“can't connect 99”，无法连接到服务端。

## 问题根因
客户端无法连接上服务端，可能与TCP连接相关的内核参数配置不合理有关。

## 解决方案
通过在客户端和服务端调整内核参数优化TCP连接性能：1. 编辑 /etc/sysctl.conf 文件；2. 添加以下参数：net.ipv4.tcp_tw_reuse = 1、net.ipv4.tcp_tw_recycle = 1、net.ipv4.tcp_syncookies = 1、net.ipv4.ip_local_port_range = 1024 65500；3. 保存文件并执行 sysctl -p 使配置生效。

