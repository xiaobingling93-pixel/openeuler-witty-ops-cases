# 使用Sysbench测试MySQL时，服务端和客户端连接不对等的解决方法

## 内核版本


## 问题现象
使用Sysbench测试MySQL，当压测的num-threads大于500时，可能会出现服务端和客户端的连接状态不对等的情况，服务端会有许多TIME_WAIT状态的进程。

## 问题根因
持续的高并发场景导致资源耗尽。

## 解决方案
1. 修改MySQL配置中的最大连接数限制，在/etc/my.cnf的[mysqld]字段下增加 max_connections=2000。
2. 调整网络相关参数：执行 echo 8192 >/proc/sys/net/ipv4/tcp_max_syn_backlog 和 echo 1024 >/proc/sys/net/core/somaxconn。
3. 修改/etc/security/limits.conf，设置用户可打开的最大文件数和最大进程数为65535：
   * soft nofile 65535
   * hard nofile 65535
   * soft nproc 65535
   * hard nproc 65535
4. 修改/etc/security/limits.d/90-nproc.conf，设置 * soft nproc 65535。
5. 重新执行Sysbench测试命令。

