# 编译HBase 1.3.0时User setting file does not exist ...\root\.m2\setting.xml的解决方法

## 内核版本


## 问题现象
执行mvn package -DskipTests assembly:single编译hbase-1.3.0-src.tar.gz时报“User setting file does not exist ...\root\.m2\setting.xml”错误。

## 问题根因
Maven在编译时尝试读取用户级别的settings.xml配置文件（位于${user.home}/.m2/settings.xml），但该文件不存在。

## 解决方案
拷贝Maven安装目录下的全局settings.xml文件到用户目录下，命令为：cp /home/apache-maven-3.5.4/conf/settings.xml /root/.m2/。Maven的settings.xml可存在于两个位置：全局配置（${maven.home}/conf/settings.xml）和用户配置（${user.home}/.m2/settings.xml），当两者共存时，用户配置为主，内容会合并。

