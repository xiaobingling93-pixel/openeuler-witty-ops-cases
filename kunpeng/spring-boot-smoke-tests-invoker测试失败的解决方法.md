# spring-boot-smoke-tests-invoker测试失败的解决方法

## 内核版本


## 问题现象
spring-boot-smoke-tests-invoker模块下载netty-transport-native-epoll-4.1.43.Final.jar失败。

## 问题根因
存储库中缺少netty-transport-native-epoll-4.1.43.Final.jar包。

## 解决方案
1. 拷贝一份netty-transport-native-epoll-4.1.43.Final.jar：\n   \cp /root/.m2/repository/io/netty/netty-transport-native-epoll/4.1.43.Final/netty-transport-native-epoll-4.1.43.Final-linux-aarch_64.jar /root/.m2/repository/io/netty/netty-transport-native-epoll/4.1.43.Final/netty-transport-native-epoll-4.1.43.Final.jar\n2. 查看netty-transport-native-epoll-4.1.43.Final.jar：\n   ls /root/.m2/repository/io/netty/netty-transport-native-epoll/4.1.43.Final/netty-transport-native-epoll-4.1.43.Final.jar\n3. 重新进行spring-boot-smoke-tests-invoker测试。

