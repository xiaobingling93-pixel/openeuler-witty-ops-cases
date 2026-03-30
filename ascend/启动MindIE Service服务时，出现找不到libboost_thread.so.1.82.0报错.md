# 启动MindIE Service服务时，出现找不到libboost_thread.so.1.82.0报错

## 内核版本


## 问题现象
启动MindIE Service服务时，系统报错提示找不到libboost_thread.so.1.82.0动态库文件。

## 问题根因
mindieservice_daemon未正确链接到其依赖的动态库（如libboost_thread.so.1.82.0），导致服务启动失败。

## 解决方案
1. 使用ldd命令检查mindieservice_daemon的动态库依赖情况；2. 执行source set_env.sh命令，设置环境变量，使mindieservice_daemon能够正确链接到所需的动态库。

