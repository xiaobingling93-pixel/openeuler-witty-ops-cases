# query过长引起日志解析结果保存失败的解决方法

## 内核版本


## 问题现象
Hive 3.1.0版本运行某些包含Group By算子的SQL时，出现'Unable to create serializer "org.apache.hive.com.esotericsoftware.kryo.serializers.FieldSerializer" for class: com.huawei.boostkit.hive.OmniGroupByOperator'错误。

## 问题根因
该问题是Kryo的bug，在Hive开源版本中也可能出现，已在Hive 4.0版本中修复。

## 解决方案
在Hive工程的pom文件中将Kryo的version改为4.0.0，重新编译打包，并替换Hive安装目录“lib”下的hive-exec-3.1.0.jar；或直接使用已编译好的Hive JAR包进行替换。

