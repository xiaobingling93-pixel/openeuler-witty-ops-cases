# 启动MindStudio时提示“WARNING: Install the haveged service by referring to the installation guide.”问题

## 内核版本


## 问题现象
启动MindStudio时提示“WARNING: Install the haveged service by referring to the installation guide.”，表示未安装haveged服务。

## 问题根因
系统熵值不足，导致ssh-manager插件在进行加解密操作时阻塞。

## 解决方案
1. 安装haveged服务：对于CentOS、OpenEuler、EulerOS、Kylin系统，执行“sudo yum install haveged”；对于Ubuntu系统，执行“sudo apt-get install haveged”。2. 检查服务状态：“systemctl status haveged.service”，若未启动则执行“systemctl start haveged.service”。3. 设置开机自启动：“systemctl enable haveged.service”。

