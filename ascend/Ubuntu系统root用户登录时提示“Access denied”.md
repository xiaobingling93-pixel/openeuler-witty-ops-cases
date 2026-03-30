# Ubuntu系统root用户登录时提示“Access denied”

## 内核版本


## 问题现象
Ubuntu系统中使用root用户通过SSH登录时，系统提示“Access denied”，无法成功登录。

## 问题根因
SSH服务配置文件/etc/ssh/sshd_config中默认禁止了root用户直接登录，配置项PermitRootLogin被设置为prohibit-password或no。

## 解决方案
1. 使用非root用户登录系统；2. 通过su命令切换到root用户；3. 编辑SSH配置文件/etc/ssh/sshd_config，将#PermitRootLogin prohibit-password修改为PermitRootLogin yes；4. 保存配置并重启服务器使配置生效。

