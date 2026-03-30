# 虚拟机安装驱动包出现报错“Drv_dkms_env_check failed”

## 内核版本
4.18.0-193.el8.x86_64

## 问题现象
在虚拟机中安装昇腾驱动包时，安装过程失败并报错“Drv_dkms_env_check failed”。日志显示驱动尝试通过DKMS重建内核模块时出错，提示需输入内核绝对路径，但即使退出后仍无法完成安装。

## 问题根因
系统缺少必要的内核头文件（kernel headers）和内核开发包（kernel-devel），导致DKMS无法正确编译驱动模块。

## 解决方案
执行命令安装内核头文件和开发包：yum install kernel-devel kernel-headers -y

