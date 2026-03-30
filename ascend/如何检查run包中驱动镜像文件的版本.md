# 如何检查run包中驱动镜像文件的版本

## 内核版本
3.10.0-957.el7.x86_64

## 问题现象
针对Atlas 200I SoC A1 核心板、Atlas 300I Pro 推理卡、Atlas 300V Pro 视频解析卡、Atlas 300I Duo 推理卡、Atlas 300V 视频解析卡产品，用户需要确认run包中驱动镜像文件的版本。

## 问题根因


## 解决方案
Driver软件包安装前：1. 以root用户上传run包到服务器；2. 解压run包（使用--noexec --extract参数）；3. 进入解压目录下的driver/host目录，执行modinfo drv_devdrv_host.ko查看版本信息。Driver软件包安装后：1. 以root用户登录；2. 执行lsmod | grep drv确认模块加载；3. 进入/lib/modules/`uname -r`/updates目录；4. 执行modinfo drv_devdrv_host查看版本信息。

