# 编译Wildfly-openssl-1.0.4.Final.jar时报错

## 内核版本


## 问题现象
编译wildfly-openssl-1.0.4.Final.jar时提示错误：../libwfssl/include/wfssl.h:41:17: fatal error: jni.h: No such file or directory。

## 问题根因
在“./libwfssl/include/”目录下未找到jni.h头文件，该文件是Java自带的JNI头文件，编译时未正确包含Java头文件路径。

## 解决方案
使用find命令全局搜索Java安装路径下的jni.h文件，并将其所在目录（通常为$JAVA_HOME/include及其平台子目录）中的相关头文件复制到“./libwfssl/include/”目录下，然后重新编译即可。

