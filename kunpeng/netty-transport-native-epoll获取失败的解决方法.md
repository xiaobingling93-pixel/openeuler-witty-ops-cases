# netty-transport-native-epoll获取失败的解决方法

## 内核版本


## 问题现象
编译过程中出现缺失libnetty_transport_native_epoll_aarch_64.so的异常，提示“Could not find artifact io.netty:netty-transport-native-epoll:jar:linux-aarch_64:4.1.43.Final...”。

## 问题根因
Spring Cloud中的一些组件（如spring-cloud-gateway、spring-cloud-gcp、spring-cloud-contract等）在编译时会拉取x86_64架构的netty-transport-native-epoll JAR包，而主流Maven仓库缺少ARM64架构版本，导致构建失败。

## 解决方案
将ARM64架构的netty-transport-native-epoll-4.1.43.Final-linux-aarch_64.jar包手动放入Maven本地仓库，并在pom.xml中添加对应依赖。具体步骤包括：1) 创建本地仓库目录；2) 从华为镜像站下载JAR包（wget https://mirrors.huaweicloud.com/kunpeng/maven/io/netty/netty-transport-native-epoll/4.1.43.Final/netty-transport-native-epoll-4.1.43.Final-linux-aarch_64.jar）；3) 复制JAR到本地仓库；4) 在pom.xml中添加带classifier为linux-aarch_64的依赖配置；5) 重新编译项目。

