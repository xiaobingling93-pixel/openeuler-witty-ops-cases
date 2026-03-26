# Atlas 800-9000 Ubuntu18.04.1 卸载加载Mellanox网卡驱动时会有错误日志打印：Failed to init debugs files for enpXX

## 内核版本


## 问题现象
在Ubuntu 18.04.1系统中，启动后以及卸载再加载Mellanox网卡驱动后，系统日志中出现两条错误信息：'Failed to init debugfs files for enp195s0f1' 和 'Failed to init debugfs files for enp195s0f0'。

## 问题根因
内核中的debugfs未启用或未正确挂载，导致Mellanox驱动在初始化调试文件时失败。

## 解决方案
检查目录 /sys/kernel/debug/mlx5/0000:c3:00.0 是否存在。若存在，说明debugfs已挂载，错误日志可忽略；若不存在，需手动执行以下操作：1. 运行命令 'mount -t debugfs none /sys/kernel/debug'；2. 在 /etc/fstab 文件中添加 'debugfs /sys/kernel/debug debugfs defaults 0 0' 以确保开机自动挂载。

