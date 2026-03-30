# 鲲鹏应用工程RSA密钥拷贝失败的解决方法

## 内核版本


## 问题现象
在使用鲲鹏DevKit工具进行RSA密钥拷贝时失败，提示错误信息如“Host key verification failed”。

## 问题根因
可能原因包括：1）用户目录（/home/devkit/.ssh/）下的known_hosts文件中记录的目标节点信息与当前系统环境不匹配；2）操作系统开启了SELinux强制模式；3）SSH端口号输入错误。

## 解决方案
1. 检查并删除用户目录下known_hosts文件中对应的目标节点信息；2. 关闭SELinux强制模式：可临时执行setenforce 0关闭，或永久修改/etc/selinux/config文件将SELINUX=enforcing改为SELINUX=disabled后重启服务器；3. 确保输入正确的SSH端口号。

