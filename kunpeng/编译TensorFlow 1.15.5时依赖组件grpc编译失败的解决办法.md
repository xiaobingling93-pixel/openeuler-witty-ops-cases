# 编译TensorFlow 1.15.5时依赖组件grpc编译失败的解决办法

## 内核版本


## 问题现象
执行编译TensorFlow 1.15.5命令时，依赖组件grpc编译失败，报错信息为：external/grpc/src/core/lib/gpr/log_linux.cc:43:13: error: ambiguating new declaration of 'long int gettid()'。

## 问题根因
依赖组件grpc中定义的gettid函数与系统库glibc中已有的gettid函数声明冲突，导致编译时出现歧义错误。

## 解决方案
1. 下载指定版本的grpc源码（https://github.com/grpc/grpc/archive/4566c2a29ebec0835643b972eb99f4306c4234a3.tar.gz）；
2. 解压后，将src/core/lib/gpr/log_posix.cc、log_linux.cc和src/core/lib/iomgr/ev_epollex_linux.cc中的gettid函数重命名为gettid_sys，可通过命令`grep -rl 'gettid' src/ | xargs sed -i 's/\bgettid/gettid_sys/g'`批量替换；
3. 重新打包修改后的grpc源码，并计算其sha256值；
4. 将新包放入本地Bazel仓库（如/home/bazel_local/）；
5. 修改TensorFlow源码中的tensorflow/workspace.bzl文件，将grpc的urls列表首项改为本地路径（如file:///home/bazel_local/grpc-...tar.gz），并更新sha256值为新包的值；
6. 重新执行bazel编译命令即可成功编译。

