# Atlas 800-3010 Redhat 7.6安装Mellanox驱动后kdump执行失败

## 内核版本
3.10.0-957.el7.x86_64

## 问题现象
在Atlas 800-3010服务器上运行Redhat 7.6系统，安装Mellanox驱动（mlx5_core 4.7-1.0.0）后，手动触发BMC NMI按键导致系统卡死，无法正常重启。串口日志显示systemd-udevd在kdump内核启动过程中因OOM（内存不足）异常终止。

## 问题根因
kdump内核启动时加载Mellanox驱动mlx5_core，该驱动在更新后内存占用增加，而kdump默认分配的内存（164MB）不足以满足其需求，导致OOM并使系统挂死。

## 解决方案
通过在/etc/sysconfig/kdump配置文件中将mlx5_core驱动加入黑名单，避免kdump内核加载该驱动。具体操作为设置KDUMP_COMMANDLINE_APPEND参数包含"modprobe.blacklist=mlx5_core"，然后执行"kdumpctl restart"重启kdump服务。

