# 编译Netty-all时可能会出现找不到jni.h和jni_md.h的报错

## 内核版本


## 问题现象
编译netty-all时可能会提示找不到jni.h和jni_md.h。

## 问题根因


## 解决方案
修改“${netty-netty-4.1.17.Final}/transport-native-unix-common/pom.xml”，找到关键字CFLAGS，加入如下参数：-I/usr/lib/jvm/java/include -I/usr/lib/jvm/java/include/linux。具体示例为：<env key="CFLAGS" value="-O3 -Werror -Wno-attributes -fPIC -fno-omit-frame-pointer -Wunused-variable -fsigned-char -I/usr/lib/jvm/java/include -I/usr/lib/jvm/java/include/linux" />

