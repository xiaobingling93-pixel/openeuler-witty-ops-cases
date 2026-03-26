# 编译TensorFlow 1.15.5时依赖组件hwloc编译失败的解决办法

## 内核版本
5.10.0

## 问题现象
执行编译TensorFlow 1.15.5命令时提示external/hwloc/hwloc/topology.c:45:10: fatal error: sys/sysctl.h: No such file or directory。

## 问题根因
头文件“sys/sysctl.h”在glibc 2.32以及之后的版本中已被删除，且Linux内核5.5版本之后也已删除“sys/sysctl.h”系统底层调用。由于编译环境内核版本为5.10.0，所以编译依赖组件hwloc报错。

## 解决方案
1. 打开并编辑“tensorflow/third_party/hwloc/BUILD.bazel”文件。
2. 按“i”进入编辑模式，删除第113行内容：“#undef HAVE_SYS_SYSCTL_H": "#define HAVE_SYS_SYSCTL_H 1”。
3. 按“Esc”键，输入:wq!，按“Enter”保存并退出编辑。
4. 重新编译TensorFlow：bazel build --config=v1 --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=0" //tensorflow/tools/pip_package:build_pip_package。

