# 容器内安装驱动时出现su命令报错

## 内核版本


## 问题现象
在Atlas系列多种硬件产品的容器内使用--docker命令安装驱动时失败，报错信息为“su: cannot open session: Critical error - immediate abort”。

## 问题根因
容器内使用su命令时，由于PAM配置中包含system-auth会话管理，而容器环境缺少相关支持，导致su命令无法正常打开会话。

## 解决方案
编辑容器内的/etc/pam.d/su文件，将“session include system-auth”这一行注释掉，保存后重新执行驱动安装操作。

