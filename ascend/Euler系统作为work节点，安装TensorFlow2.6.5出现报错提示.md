# Euler系统作为work节点，安装TensorFlow2.6.5出现报错提示

## 内核版本


## 问题现象
Euler系统作为work节点，在安装TensorFlow2.6.5时出现报错提示“Failed to connect to the host via ssh: Shared connection to XX closed”。

## 问题根因
主机中设置了SSH连接会话超时时间，当部署任务的执行时间超过该超时时间时，SSH连接被关闭，导致报错。

## 解决方案
修改“/etc/ssh/sshd_config”文件中的“ClientAliveInterval”参数值为“1800”（即30分钟），然后执行命令“systemctl restart sshd”重启sshd服务。

