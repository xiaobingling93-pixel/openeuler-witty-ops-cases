# NPU Exporter检查动态路径失败，日志出现check uid or mode failed

## 内核版本


## 问题现象
执行kubectl get pod -A | grep npu-exporter命令显示NPU Exporter容器处于CrashLoopBackOff状态；查看日志发现报错信息为“cannot found valid driver lib, fromEnv: lib path is invalid, [/usr/local: check uid or mode failed; /usr/local: check uid or mode failed;], fromLdCmd: can't find valid lib”，表明NPU Exporter启动时无法正确访问驱动库路径，因目录权限校验失败导致初始化失败。

## 问题根因
容器镜像内/usr/local目录的权限设置不正确（权限为777），导致NPU Exporter在启动过程中执行安全检查时因“uid or mode”校验失败而无法加载所需的驱动库文件。

## 解决方案
1. 通过docker ps -a | grep npu-exporter获取容器ID；2. 使用docker run -it <镜像ID> bash进入容器；3. 执行ll /usr/确认/usr/local目录权限异常；4. 执行chmod 755 /usr/local修正权限；5. 退出容器后使用docker commit <容器ID> npu-exporter:v{version}提交修改；6. 等待或手动重启Pod使新镜像生效；7. 验证Pod状态恢复正常后，删除临时容器副本。

