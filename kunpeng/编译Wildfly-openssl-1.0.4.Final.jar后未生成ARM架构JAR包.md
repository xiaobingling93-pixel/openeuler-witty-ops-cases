# 编译Wildfly-openssl-1.0.4.Final.jar后未生成ARM架构JAR包

## 内核版本


## 问题现象
编译wildfly-openssl-1.0.4.Final.jar后未生成ARM架构JAR包。

## 问题根因
源码中的pom.xml文件未定义linux-aarch64模块，需手动添加对ARM架构的支持。

## 解决方案
1. 创建“linux-aarch64”目录；2. 将linux-x86_64下的Makefile和pom.xml复制到该目录；3. 修改./pom.xml、./combined/pom.xml、./java/pom.xml、./linux-aarch64/pom.xml和./linux-aarch64/Makefile文件，增加对linux-aarch64的配置支持；4. 重新执行编译命令；5. 验证生成的JAR包是否包含ARM架构支持。

