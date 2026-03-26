# AI应用进程未退出，导致休眠唤醒失败

## 内核版本


## 问题现象
系统休眠失败。查看应用类日志发现任务分发模块hwts处于busy状态，不满足休眠条件，日志显示“suspend pre check fail, hwts is busy”和“ts suspend ack ret=1”。

## 问题根因
休眠前AI应用进程未退出，导致相关硬件资源未处于idle态，系统检测到hwts处于busy状态，因此拒绝进入休眠。

## 解决方案
确保AI应用进程已运行结束或优雅退出，推荐使用“kill -2 PID”命令终止相关进程（PID需替换为实际进程ID）。

