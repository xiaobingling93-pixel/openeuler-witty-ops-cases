# 使用鲲鹏兼容性测试工具提示apt源或yum源不可用问题的解决方法

## 内核版本


## 问题现象
在使用鲲鹏兼容性测试工具时，提示apt源或yum源不可用，导致无法安装工具所需的依赖软件包。

## 问题根因
系统未正确配置可用的本地或远程软件源（如apt源、yum源或zypper源），导致无法下载和安装测试工具依赖的软件包。

## 解决方案
根据操作系统类型配置可用的软件源后，执行对应的依赖安装命令：
- CentOS/中标麒麟/openEuler/银河麒麟v10：运行 `yum -y install nmap ipmitool dmidecode pciutils util-linux net-tools sysstat bc`
- Ubuntu/银河麒麟 4.0.2 /UOS：运行 `apt -y install nmap ipmitool dmidecode lspci lscpu lsblk ifconfig netstat sysstat bc`
- SUSE：运行 `zypper install -y nmap ipmitool dmidecode lspci lscpu lsblk ifconfig netstat sysstat bc`

