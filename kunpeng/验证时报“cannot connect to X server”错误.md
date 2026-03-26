# 验证时报“cannot connect to X server”错误

## 内核版本


## 问题现象
运行验证中报错“PipedViewerPQ: cannot connect to X server”。

## 问题根因
X11-forwarding未开启。

## 解决方案
1. 执行CTRL+Z退出当前界面。
2. 安装必要的X11相关软件包：yum install -y xorg-x11-xauth xorg-x11-fonts* xorg-x11-font-utils xorg-x11-fonts-Type1 xclock。
3. 修改/etc/ssh/sshd_config文件，将X11Forwarding设置为yes，并保存退出。
4. 重启sshd服务：systemctl restart sshd。
5. 重新连接服务器并执行验证步骤。

