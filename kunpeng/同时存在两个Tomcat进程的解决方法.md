# 同时存在两个Tomcat进程的解决方法

## 内核版本


## 问题现象
查看Tomcat进程时，发现系统中同时存在两个Tomcat进程。

## 问题根因
Tomcat不能通过kill命令直接停止，必须使用shutdown.sh脚本停止。由于上一次启动的Tomcat进程未被成功停止，导致再次启动时出现两个Tomcat进程。

## 解决方案
1. 使用shutdown.sh脚本停止Tomcat进程：sh shutdown.sh；2. 再次检查Tomcat进程是否已全部停止：ps -ef | grep tomcat。

