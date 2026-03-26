# Jenkins工作节点连接失败的解决方法

## 内核版本


## 问题现象
Jenkins工作节点连接失败，日志显示与SSH主机密钥验证相关的问题（参见图1）。

## 问题根因
已安装Jenkins服务的设备上未配置known_hosts文件，导致无法验证远程工作节点的SSH主机密钥。

## 解决方案
1. 临时断开连接失败的工作节点；2. 在Jenkins服务器上创建并配置/var/lib/jenkins/.ssh/known_hosts文件：mkdir -p /var/lib/jenkins/.ssh；touch /var/lib/jenkins/.ssh/known_hosts；chmod 600 /var/lib/jenkins/.ssh/known_hosts；使用ssh-keyscan <目标服务器IP地址> >> /var/lib/jenkins/.ssh/known_hosts 添加远程主机密钥；chown -R jenkins:jenkins /var/lib/jenkins/.ssh 修改文件属主；3. 重新上线工作节点，完成连接恢复。

