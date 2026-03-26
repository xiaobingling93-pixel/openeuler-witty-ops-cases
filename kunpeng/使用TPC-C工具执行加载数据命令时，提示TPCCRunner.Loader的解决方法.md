# 使用TPC-C工具执行加载数据命令时，提示TPCCRunner.Loader的解决方法

## 内核版本


## 问题现象
在执行java -cp bin/:lib/mysql-connector-java-5.1.7-bin.jar iomark.TPCCRunner.Loader conf/example/mysql/loader.properties时，提示“Error: Could not find or load main class iomark.TPCCRunner.Loader”。

## 问题根因
类路径中无法找到指定的主类，需要设置正确的类路径。

## 解决方案
执行加载数据命令时，在目录中添加JAR包的名称，具体命令为：java -cp bin/TPCC_CMCC_v2.jar:lib/mysql-connector-java-5.1.7-bin.jar iomark.TPCCRunner.Loader conf/example/mysql/loader.properties

