# Ubuntu系统Attach to Process模式下调试失败的解决方法

## 内核版本


## 问题现象
在Ubuntu系统下，连接被调试节点的普通用户时，创建Attach调试任务失败。

## 问题根因
系统默认配置导致相关权限不足，具体为kernel.yama.ptrace_scope参数值不为0，限制了非特权进程对其他进程的ptrace操作。

## 解决方案
1. 编辑“/etc/sysctl.d/10-ptrace.conf”文件；2. 将“kernel.yama.ptrace_scope = 0”写入文件；3. 保存并退出；4. 执行“service procps restart”重启procps服务以使配置生效。

