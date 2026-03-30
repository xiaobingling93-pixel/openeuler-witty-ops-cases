# 找不到jni.h或者jni_md.h的解决方法

## 内核版本


## 问题现象
提示找不到jni.h或者jni_md.h。

## 问题根因
没有配置JAVA_HOME路径。

## 解决方案
请参见《Hadoop移植指南（CentOS&openEuler）》中“安装OpenJDK”章节配置JAVA_HOME路径后重新编译。如果还出错，则将编译使用JDK中的jni.h和jni_md.h移动到编译根目录。

