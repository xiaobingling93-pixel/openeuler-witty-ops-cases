# 执行sysctl -p时提示没有文件或目录的解决方法

## 内核版本


## 问题现象
修改了“/etc/sysctl.conf”之后，执行生效命令sysctl -p时，提示“No such file or directory”。

## 问题根因
部署Neutron时，需要开启网桥筛选的功能，在系统配置文件中添加了“net.ipv4.conf.all.rp_filter = 0 net.ipv4.conf.default.rp_filter = 0”，但系统未安装br_netfilter驱动，导致相关内核参数无法识别。

## 解决方案
1. 安装br_netfilter驱动：执行“modprobe br_netfilter”后再运行“sysctl -p”。
2. 为确保重启后模块自动加载，新建并编辑“/etc/rc.sysinit”文件，内容为：
#!/bin/bash
for file in /etc/sysconfig/modules/*.modules ; do
[ -x $file ] && $file
done
3. 新建并编辑“/etc/sysconfig/modules/br_netfilter.modules”文件，内容为：“modprobe br_netfilter”。
4. 增加执行权限：“chmod 755 /etc/sysconfig/modules/br_netfilter.modules”。

