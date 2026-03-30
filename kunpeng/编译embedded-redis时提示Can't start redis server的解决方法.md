# 编译embedded-redis时提示Can't start redis server的解决方法

## 内核版本


## 问题现象
编译embedded-redis时，执行mvn install命令后失败，提示“Can't start redis server”。

## 问题根因
端口被占用导致的问题。

## 解决方案
1. 查看Redis进程：ps -ef | grep redis
2. 关闭Redis进程：pkill redis
3. 再次查看Redis进程确认已关闭：ps -ef | grep redis
4. 重新编译embedded-redis。

