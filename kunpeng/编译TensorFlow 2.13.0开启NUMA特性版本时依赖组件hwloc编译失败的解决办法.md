# 编译TensorFlow 2.13.0开启NUMA特性版本时依赖组件hwloc编译失败的解决办法

## 内核版本
5.10.0

## 问题现象
在编译TensorFlow 2.13.0开启NUMA支持时，依赖组件hwloc编译失败，报错信息为：external/hwloc/hwloc/topology.c:49:10: fatal error: sys/sysctl.h: No such file or directory。

## 问题根因
头文件“sys/sysctl.h”在glibc 2.32及之后版本中已被移除，且Linux内核5.5之后也删除了对该头文件的底层支持。当前编译环境内核版本为5.10.0，因此hwloc组件在编译时因找不到该头文件而失败。

## 解决方案
编辑TensorFlow源码目录下的third_party/hwloc/hwloc.BUILD文件，删除第113行的"#undef HAVE_SYS_SYSCTL_H": "#define HAVE_SYS_SYSCTL_H 1"，然后重新执行编译命令：bazel build //tensorflow/tools/pip_package:build_pip_package --config=numa。

