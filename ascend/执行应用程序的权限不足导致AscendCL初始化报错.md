# 执行应用程序的权限不足导致AscendCL初始化报错

## 内核版本


## 问题现象
用户进程报错并退出，应用日志显示获取Device信息失败，AscendCL初始化失败，错误码包括507008和107002，提示“ctx is NULL!”和“context pointer null”。

## 问题根因
执行应用程序的用户权限不足，无法查询Device信息；或者Device状态异常未正常启动。

## 解决方案
1. 确认Device是否正常启动：以root用户查看/etc/ascend_install.info获取Driver安装路径，使用upgrade-tool --device_index -1 --system_version检查Device侧文件系统版本。2. 检查运行应用程序的用户权限：确保该用户与Driver运行用户（默认HwHiAiUser）在同一属组，可通过usermod -g 组名 用户名调整。3. 若问题仍未解决，设置ASCEND_GLOBAL_LOG_LEVEL=0收集Debug日志，并使用msnpureport工具获取Device上的详细日志，通过ModelZoo仓提Issue反馈。

