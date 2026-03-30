# 如何检查Device是否正常运行

## 内核版本


## 问题现象
在Atlas系列硬件（如Atlas 200I A2加速模块、Atlas 300I Pro推理卡、Atlas 800训练服务器等）环境中，用户需要确认Device是否已正常启动和运行。

## 问题根因


## 解决方案
1. 以root用户登录运行环境；2. 执行命令 cat /etc/ascend_install.info 获取驱动安装路径；3. 进入驱动路径下的tools目录，执行 ./upgrade-tool --device_index -1 --system_version 查询Device侧文件系统版本；若能正常返回版本信息，则说明Device已正常启动。

