# 启动OVS过程提示ovs-ctl command not found的解决方法

## 内核版本


## 问题现象
输入命令ovs-ctl start，提示“ovs-ctl command not found”。

## 问题根因
未设置工具路径至环境变量。

## 解决方案
1. 确认Open vSwitch安装路径，例如“/usr/local/share”。
2. 设置环境变量：export PATH=$PATH:/usr/local/share/openvswitch/scripts。
3. 重新启动OVS组件：ovs-ctl start。

