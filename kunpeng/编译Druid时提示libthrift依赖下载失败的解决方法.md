# 编译Druid时提示libthrift依赖下载失败的解决方法

## 内核版本


## 问题现象
编译Druid过程中，Maven构建失败，提示无法解析插件com.twitter:scrooge-maven-plugin:4.11.0的依赖org.apache.thrift:libthrift:jar:0.5.0-1，具体错误为无法从maven.twttr.com仓库下载该依赖的POM文件。

## 问题根因
org.apache.thrift:libthrift:0.5.0-1 依赖已无法从默认配置的 Maven 仓库（如 maven.twttr.com）中获取，可能是仓库地址失效或该版本未在公共仓库中发布。

## 解决方案
手动下载包含所需libthrift版本的maven-repo，将其中的“org/apache/thrift”目录替换本地Maven仓库中对应的thrift目录，以提供缺失的依赖。

