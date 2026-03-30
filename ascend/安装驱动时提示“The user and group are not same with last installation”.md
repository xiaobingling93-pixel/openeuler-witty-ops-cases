# 安装驱动时提示“The user and group are not same with last installation”

## 内核版本


## 问题现象
安装驱动时出现“The user and group are not same with last installation, do not support overwriting installation”提示信息。

## 问题根因
当前指定的驱动运行用户与“/etc/ascend_install.info”文件中记录的运行用户不一致，导致校验失败，安装退出。根本原因是之前卸载驱动和CANN软件时，aicpu没有被卸载，导致“/etc/ascend_install.info”文件未清空。

## 解决方案
先卸载aicpu，再安装驱动：1. 以root用户登录安装环境；2. 进入卸载脚本所在目录（cd /usr/local/Ascend/opp/aicpu/script）；3. 执行./uninstall.sh命令运行脚本，完成卸载。

