# 编译Druid时提示hadoop-lzo依赖下载报错

## 内核版本


## 问题现象
编译Druid过程中提示无法解析依赖项com.hadoop.gplcompression:hadoop-lzo:jar:0.4.19，具体错误为无法从http://maven.twttr.com下载该依赖的POM文件，返回502 Bad Gateway错误。

## 问题根因


## 解决方案
修改本地Maven仓库中elephant-bird-4.8.pom文件（路径：./repository/com/twitter/elephantbird/elephant-bird/4.8/elephant-bird-4.8.pom），将其中twitter仓库的URL从http://maven.twttr.com替换为https://nexus.xebialabs.com/nexus/content/groups/public/，以解决依赖下载失败的问题。

