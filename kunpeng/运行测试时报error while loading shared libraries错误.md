# 运行测试时报error while loading shared libraries错误

## 内核版本


## 问题现象
运行测试时报错，报错信息类似：“error while loading shared libraries: libhts.so.2: cannot open shared object file: No such file or directory”。

## 问题根因
未增加htslib环境变量。

## 解决方案
1. 使用PuTTY工具，以root用户登录服务器。
2. 执行以下命令指定htslib地址：export LD_LIBRARY_PATH=/path/to/HTSLIB/htslib-1.9:$LD_LIBRARY_PATH

