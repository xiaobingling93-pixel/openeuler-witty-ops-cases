# 编译Bazel 0.26.1失败的解决办法

## 内核版本


## 问题现象
编译Bazel 0.26.1时提示error: ambiguating new declaration of 'long int gettid()'。

## 问题根因
Bazel源码定义的gettid()函数与glibc库冲突。

## 解决方案
将Bazel源码中的函数名gettid改为gettid_sys，再重新编译Bazel。具体操作为执行命令：grep -rl 'gettid' third_party/grpc/src/ | xargs sed -i 's/\bgettid/gettid_sys/g'。

