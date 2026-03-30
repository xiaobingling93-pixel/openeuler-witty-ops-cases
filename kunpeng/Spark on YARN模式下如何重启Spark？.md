# Spark on YARN模式下如何重启Spark？

## 内核版本


## 问题现象
在Spark on YARN模式下需要重启Spark服务。

## 问题根因


## 解决方案
1. 进入到Spark目录下的sbin目录（例如：/usr/local/spark/sbin/）；2. 执行./stop-all.sh停止Spark；3. 执行./start-all.sh启动Spark，完成重启。

