# 启动MindStudio时无法显示图形化界面

## 内核版本


## 问题现象
启动MindStudio时，出现“Failed to initialize graphics environment”、“Unable to detect graphics environment”或“Can't connect to X11 window server using 'localhost:xxx' as the value of the DISPLAY variable”等报错信息，导致无法显示图形化界面。

## 问题根因
可能的原因包括：1）使用某用户登录了MobaXterm，图形工具被该用户组占用，切换用户后无法使用；2）登录用户与启动MindStudio的用户不一致；3）未安装X11-forwarding依赖；4）SSH未开启X11Forwarding；5）$HOME/.Xauthority为文件夹而非文件。

## 解决方案
1. 若因MobaXterm用户占用图形资源，可将新用户加入原用户组，或直接用目标用户登录MobaXterm并启动MindStudio；2. 确保使用登录系统的同一用户启动MindStudio；3. 安装X11依赖：Red Hat/OpenEuler系统执行 yum install xorg-x11-xauth，Ubuntu系统执行 apt-get install x11-apps；4. 修改/etc/ssh/sshd_config，设置 X11Forwarding yes（CentOS 7.6/Euler2.8还需设 X11UseLocalhost no），然后重启ssh服务（Red Hat/OpenEuler: service sshd restart；Ubuntu: service ssh restart）；5. 若$HOME/.Xauthority是文件夹，删除该文件夹。

