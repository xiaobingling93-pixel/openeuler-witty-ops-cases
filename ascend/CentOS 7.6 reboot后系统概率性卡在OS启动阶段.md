# CentOS 7.6 reboot后系统概率性卡在OS启动阶段

## 内核版本


## 问题现象
Atlas 800 训练服务器（型号：9000）、Atlas 800 训练服务器（型号：9010）、Atlas 900 计算节点、Atlas 900T RAK 计算节点在驱动或固件安装后，CentOS 7.6系统执行reboot时概率性卡在OS启动阶段，串口打印如图所示；再次强制重启进入系统后，发现/proc/sys/kernel/printk的打印权限为“7 4 1 7”。

## 问题根因
CentOS 7.6系统打印权限过低，导致启动阶段串口打印过多，从而引发OS启动卡死。

## 解决方案
使用root用户登录操作系统，执行命令 echo "3 4 1 7" > /proc/sys/kernel/printk 修改内核打印权限配置。

