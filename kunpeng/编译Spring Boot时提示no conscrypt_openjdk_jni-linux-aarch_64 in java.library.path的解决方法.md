# 编译Spring Boot时提示no conscrypt_openjdk_jni-linux-aarch_64 in java.library.path的解决方法

## 内核版本


## 问题现象
编译Spring Boot过程中出现“java.lang.UnsatisfiedLinkError: no conscrypt_openjdk_jni-linux-aarch_64 in java.library.path”的异常，原因是所使用的conscrypt-openjdk-uber-2.1.0.jar包不包含ARM64架构所需的so文件。

## 问题根因
原始的conscrypt-openjdk-uber-2.1.0.jar包不支持ARM64架构，缺少对应的native库（so文件）。

## 解决方案
1. 创建目录“/root/.m2/repository/org/conscrypt/conscrypt-openjdk-uber/2.1.0”。
2. 从华为镜像站下载支持ARM64架构的jar包：wget https://mirrors.huaweicloud.com/kunpeng/maven/org/conscrypt/conscrypt-openjdk-uber/2.1.0/conscrypt-openjdk-uber-2.1.0.jar --no-check-certificate。
3. 将下载的jar包拷贝至上述目录：\cp conscrypt-openjdk-uber-2.1.0.jar /root/.m2/repository/org/conscrypt/conscrypt-openjdk-uber/2.1.0。
4. 重新编译Spring Boot项目。

