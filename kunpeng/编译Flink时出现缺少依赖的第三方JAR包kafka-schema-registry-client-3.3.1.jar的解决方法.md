# 编译Flink时出现缺少依赖的第三方JAR包kafka-schema-registry-client-3.3.1.jar的解决方法

## 内核版本


## 问题现象
编译Flink时提示错误：Failed to execute goal on project flink-avro-confluent-registry: Could not resolve dependencies for project org.apache.flink:flink-avro-confluent-registry:jar:1.8.1: Could not find artifact io.confluent:kafka-schema-registry-client:jar:3.3.1 in big (http://10.93.238.51/maven/)

## 问题根因
缺少依赖的第三方JAR包kafka-schema-registry-client-3.3.1.jar

## 解决方案
下载kafka-schema-registry-client-3.3.1.jar，保存到Maven仓库或者本地缓存库“*/.m2/repository/io/confluent/kafka-schema-registry-client/3.3.1”目录下，重新编译Flink。

