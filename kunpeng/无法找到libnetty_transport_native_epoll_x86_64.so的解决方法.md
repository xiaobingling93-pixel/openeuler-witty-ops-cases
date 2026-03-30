# 无法找到libnetty_transport_native_epoll_x86_64.so的解决方法

## 内核版本


## 问题现象
构建过程中提示找不到文件：/opt/tools/installed/hbase-thirdparty-rel-2.1.0/hbase-shaded-netty/target/unpacked/META-INF/native/libnetty_transport_native_epoll_x86_64.so。

## 问题根因
在非x86架构（如ARM aarch64）环境下，Netty尝试加载x86_64版本的native库，但实际应使用对应架构的aarch64版本，导致文件路径不匹配而报错。

## 解决方案
编辑hbase-shaded-netty/pom.xml文件，将其中引用的libnetty_transport_native_epoll_x86_64.so替换为libnetty_transport_native_epoll_aarch_64.so，保存后重新构建。

