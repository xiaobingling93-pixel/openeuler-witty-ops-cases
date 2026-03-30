# 系统日志dmesg提示nf_conntrack: table full, dropping packet的解决方法

## 内核版本


## 问题现象
系统日志dmesg提示“nf_conntrack: table full, dropping packet”。

## 问题根因
nf_conntrack跟踪表已满。

## 解决方案
将Linux系统中的连接跟踪最大数限制设置为0，即禁用连接跟踪功能。具体操作：1. 在内核配置文件“/etc/sysctl.conf”中加入代码：net.netfilter.nf_conntrack_max=0；2. 执行命令 sysctl -p 使配置生效。

