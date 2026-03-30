# 启动VNC时出现“Oh no! Something has gone wrong.”报错

## 内核版本


## 问题现象
在Linux系统上，使用“VNC方式”启动MindStudio Insight时，启动VNC后弹出“Oh no! Something has gone wrong.”错误窗口。

## 问题根因
SSH服务端的AllowTcpForwarding选项未开启。VNC在某些情况下需要通过SSH通道实现连接，而TCP转发是支持该功能的关键。若AllowTcpForwarding被关闭，SSH将不允许端口转发，导致无法通过SSH通道访问VNC服务。

## 解决方案
配置SSH服务端：1. 进入/etc/ssh目录，打开sshd_config文件；2. 将AllowTcpForwarding修改为“yes”；3. 执行systemctl restart sshd命令重启SSH服务；4. 重启成功后，重新打开新窗口启动VNC。

