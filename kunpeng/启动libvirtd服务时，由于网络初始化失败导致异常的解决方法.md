# 启动libvirtd服务时，由于网络初始化失败导致异常的解决方法

## 内核版本


## 问题现象
启动libvirtd服务后，服务立即变为inactive (dead)状态，无法连接到hypervisor。执行virsh version命令报错：'error: failed to connect to the hypervisor' 和 'error: Failed to connect socket to '/var/run/libvirt/libvirt-sock': No such file or directory'。

## 问题根因
libvirtd服务在初始化过程中因网络配置问题失败。日志显示两个关键错误：1) 网络'default'已存在且UUID冲突（'network 'default' already exists with uuid ...'）；2) netcf状态驱动初始化失败（'internal error: failed to initialize netcf'），导致整个驱动状态初始化失败，服务退出。

## 解决方案
通过重启网络服务解决依赖问题：1) 执行'service network restart'重启网络服务；2) 再次执行'service libvirtd restart'重启libvirtd服务；3) 验证服务是否正常，执行'virsh version'应能正确显示libvirt和QEMU版本信息。

