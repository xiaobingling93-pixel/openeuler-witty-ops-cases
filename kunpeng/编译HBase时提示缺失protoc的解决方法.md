# 编译HBase时提示缺失protoc的解决方法

## 内核版本


## 问题现象
protobuf-2.5.0已安装，但编译HBase时提示缺失protoc，错误信息为：[ERROR] Failed to execute goal org.xolstice.maven.plugins:protobuf-maven-plugin:0.5.0:compile(compile-protoc) on project hbase-protocol: Missing。

## 问题根因
未安装protoc组件或protoc未正确注册为Maven本地依赖。

## 解决方案
手动将protoc注册为Maven本地依赖，执行命令：mvn install:install-file -DgroupId=com.google.protobuf -DartifactId=protoc -Dversion=2.5.0 -Dclassifier=linux-aarch_64 -Dpackaging=exe -Dfile=/usr/bin/protoc。

