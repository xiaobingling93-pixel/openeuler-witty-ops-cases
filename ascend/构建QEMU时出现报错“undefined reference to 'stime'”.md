# 构建QEMU时出现报错“undefined reference to 'stime'”

## 内核版本


## 问题现象
在构建QEMU（版本4.1.0）时，链接阶段报错“undefined reference to 'stime'”，具体发生在linux-user/syscall.c文件的do_syscall1函数中调用stime函数时，导致编译失败。

## 问题根因
stime函数在较新的glibc版本中已被移除或弃用，而QEMU源码中仍直接调用该函数，导致链接时找不到符号定义。

## 解决方案
修改./linux-user/syscall.c文件中TARGET_NR_stime对应的代码块，将对stime函数的调用替换为使用clock_settime(CLOCK_REALTIME, &res)的方式设置系统时间。具体做法是：将host_time赋值给timespec结构体的tv_sec字段，然后调用clock_settime函数。

