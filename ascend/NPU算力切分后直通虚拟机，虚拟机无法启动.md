# NPU算力切分后直通虚拟机，虚拟机无法启动

## 内核版本


## 问题现象
虚拟机openEuler 20.03 LTS在NPU算力切分后直通虚拟机时无法启动，系统日志显示内核调用栈异常，涉及__schedule、schedule_timeout和work_func等函数。

## 问题根因
set_cpus_allowed_ptr函数在执行CPU切换或切换过程中出现调用栈异常，导致虚拟机启动失败。

## 解决方案
下载并应用指定的内核补丁（6d25be5782e482eb93e3de0c94d0a517879377d0.patch），重新编译安装内核后重启系统。

