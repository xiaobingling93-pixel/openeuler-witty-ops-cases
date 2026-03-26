# 编译Redis失败，无法启动redis服务器的解决方法

## 内核版本


## 问题现象
编译Redis时，由于运行时无法启动Redis服务器而编译失败，提示“Runtime Can't start redis server”。

## 问题根因
编译Redis时，需要使用支持aarch64的embedded-redis-0.6.jar包，但本地仓库中的jar包不支持aarch64架构。

## 解决方案
1. 获取支持aarch64的embedded-redis-0.6.jar包：
   cd /home
   wget https://mirrors.huaweicloud.com/kunpeng/maven/com/github/kstyrc/embedded-redis/0.6/embedded-redis-0.6.jar --no-check-certificate
2. 替换本地仓库中的jar包：
   \cp /home/embedded-redis-0.6.jar /root/.m2/repository/com/github/kstyrc/embedded-redis/0.6/embedded-redis-0.6.jar
3. 重新编译Redis模块：
   cd /home/Dubbo/dubbo-dubbo-2.6.8/dubbo-rpc/dubbo-rpc-redis
   mvn install
   若显示BUILD SUCCESS，则编译成功。

