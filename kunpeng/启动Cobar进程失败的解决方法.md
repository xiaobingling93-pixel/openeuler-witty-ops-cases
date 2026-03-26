# 启动Cobar进程失败的解决方法

## 内核版本


## 问题现象
启动Cobar进程失败，执行命令./startup.sh后，查看stdout.log文件，提示“The stack size specified is too small, Specify at least 328k”、“Error: Could not create the Java Virtual Machine.”以及“Error: A fatal exception has occurred. Program will exit.”

## 问题根因
启动Java虚拟机时指定的线程栈大小（-Xss）过小，低于JVM要求的最小值（至少328k），导致无法创建Java虚拟机。

## 解决方案
进入/home/cobar-server-1.2.8-SNAPSHOT/bin目录，编辑startup.sh文件，将第38行的JAVA_OPTS参数中的-Xss值修改为至少328k，例如：JAVA_OPTS="-server -Xms10240m -Xmx10240m -Xmn8g -Xss328k"，保存后重新执行./startup.sh启动Cobar进程。

