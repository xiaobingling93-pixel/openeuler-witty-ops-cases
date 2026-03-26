# 安装MySQL线程池插件时提示undefined symbol: numa_num_configured_cpus的解决方法

## 内核版本


## 问题现象
在安装MySQL线程池插件时，执行INSTALL PLUGIN thread_pool SONAME "thread_pool.so";语句报错：Can't open shared library '/usr/local/mysql/lib/plugin/thread_pool.so' (errno: 2 /usr/local/mysql/lib/plugin/thread_pool.so: undefined symbol: numa_num_configured_cpus)。

## 问题根因
MySQL在编译时未安装numactl依赖库，导致生成的程序缺少对NUMA库的支持，因此在加载线程池插件（thread_pool.so）时无法找到符号numa_num_configured_cpus。

## 解决方案
1. 安装numactl库：yum install -y numactl numactl-devel*；2. 重新编译MySQL，具体操作参考《MySQL 8.0.x 移植指南》。

