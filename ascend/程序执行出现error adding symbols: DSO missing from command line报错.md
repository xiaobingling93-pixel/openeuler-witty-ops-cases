# 程序执行出现error adding symbols: DSO missing from command line报错

## 内核版本


## 问题现象
在Vision SDK 6.0.RC1之前版本的部分操作系统上执行程序时，出现报错：{Visionsdk安装路径}/lib/libcpprest.so.2.10: error adding symbols: DSO missing from command line。

## 问题根因
由于cpprest开源软件消减，无法找到所需的库文件。

## 解决方案
执行如下命令，配置环境变量：export LDFLAGS="-Wl,--copy-dt-needed-entries"。

