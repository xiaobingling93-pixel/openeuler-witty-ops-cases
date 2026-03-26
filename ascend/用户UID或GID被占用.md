# 用户UID或GID被占用

## 内核版本


## 问题现象
用户的UID或者GID被其他用户占用了。

## 问题根因


## 解决方案
如果用户是HwHiAiUser，建议将驱动、固件卸载后，再按照修改hwMindX用户的UID和GID的方法，修改HwHiAiUser用户的UID和GID，然后再重装驱动和固件。如果用户是hwMindX，首先修改当前占用9000的用户的UID和GID为其他值（例如将test用户的UID和GID修改为1001），并更新相关文件属主；然后将hwMindX用户的UID和GID修改为9000，并更新其原UID/GID对应的文件属主。

