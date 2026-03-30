# Ubuntu系统HPC应用分析任务数据采集失败的解决方法

## 内核版本
4.15.0

## 问题现象
在Ubuntu系统上执行HPC应用分析任务时，数据采集失败。

## 问题根因
Ubuntu 13.04及以后版本默认禁用了perf工具中的Python scripting功能，导致HPC应用分析任务无法正常采集数据。

## 解决方案
1. 以root用户登录系统，使用uname -r命令确认当前内核版本（例如4.15.0）；
2. 创建目录并下载对应内核版本的Linux源码：mkdir /home/linux_kernel && cd /home/linux_kernel && apt-get update && apt-get source linux-source-<kernel-version>；
3. 进入perf目录（如/home/linux_kernel/linux-4.15.0/tools/perf），执行make查看缺失依赖；
4. 安装所需依赖包：apt-get install python-dev libelf-dev libunwind-dev libaudit-dev libslang2-dev；
5. 再次编译并安装perf：make && make install；
6. 验证编译是否成功：执行perf record和perf script -g python，确认生成perf-script.py文件；
7. 将新编译的perf替换系统原有perf：cp /home/linux_kernel/linux-<kernel-version>/tools/perf/perf /usr/bin。

