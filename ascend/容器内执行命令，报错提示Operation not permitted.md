# 容器内执行命令，报错提示Operation not permitted

## 内核版本


## 问题现象
在容器内运行脚本时，执行某些命令会报错“Operation not permitted”。

## 问题根因
容器内的用户权限受限，可能由于seccomp安全策略限制了部分系统调用（如chmod、mount），或容器未以足够权限启动。

## 解决方案
可尝试以下方法解决：1. 升级Docker到新版本（如v28.1.1），但该问题通常与安全策略或文件权限相关，升级不一定有效；2. 在docker run命令中添加--security-opt seccomp=unconfined以关闭seccomp限制；3. （仅限开发环境）使用--privileged=true启动特权容器，赋予容器近乎完整的宿主机内核权限，但存在安全风险，不推荐长期使用。

