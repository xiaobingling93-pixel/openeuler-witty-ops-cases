# 创建uid和gid为1000的驱动运行用户HwHiAiUser失败

## 内核版本


## 问题现象
在创建UID和GID均为1000的驱动运行用户HwHiAiUser时失败，系统返回错误信息：groupadd：GID '1000' already exists。

## 问题根因
UID和GID为1000的标识已被系统中其他用户（如示例中的st用户）占用，导致无法重复分配给新用户HwHiAiUser。

## 解决方案
1. 使用命令 cat /etc/passwd | grep 1000 查看占用1000 UID/GID的用户；2. 使用 usermod -u 1002 <用户名> 和 groupmod -g 1002 <用户名> 修改该用户的UID和GID（以1002为例）；3. 确认1000已释放后，执行 groupadd -g 1000 HwHiAiUser 和 useradd -g HwHiAiUser -u 1000 -d /home/HwHiAiUser -m HwHiAiUser -s /bin/bash 创建所需用户。

