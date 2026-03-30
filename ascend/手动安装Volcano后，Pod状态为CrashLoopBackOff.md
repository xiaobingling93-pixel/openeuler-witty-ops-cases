# 手动安装Volcano后，Pod状态为CrashLoopBackOff

## 内核版本


## 问题现象
Volcano在运行时，其Pod状态为“CrashLoopBackOff”。查看对应Pod日志发现“permission denied”报错，并伴随streamwatcher.go等待超时。

## 问题根因
手动安装时，Volcano的日志目录权限设置不正确，导致组件无法正常写入日志文件。

## 解决方案
执行以下命令修复volcano-controller组件的日志目录权限：chown -R hwMindX:hwMindX /var/log/mindx-dl/volcano-controller；chmod 750 /var/log/mindx-dl/volcano-volcano-controller；chmod 640 /var/log/mindx-dl/volcano-volcano-controller/volcano-controller.log。同样地，为volcano-scheduler组件执行类似操作：chown -R hwMindX:hwMindX /var/log/mindx-dl/volcano-scheduler；chmod 750 /var/log/mindx-dl/volcano-scheduler；chmod 640 /var/log/mindx-dl/volcano-scheduler/volcano-scheduler.log。之后等待Pod自动恢复或手动删除异常Pod触发重建。

