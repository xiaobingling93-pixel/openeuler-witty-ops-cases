# 下载gradle-5.6-bin.zip失败

## 内核版本


## 问题现象
执行./gradlew shadowJar命令时因网络访问失效导致无法下载gradle-5.6-bin.zip，出现报错。

## 问题根因
网络访问失效，无法从https://services.gradle.org/distributions/gradle-5.6-bin.zip下载所需文件。

## 解决方案
1. 手动使用wget命令下载gradle-5.6-bin.zip到当前目录：wget https://services.gradle.org/distributions/gradle-5.6-bin.zip；2. 修改./gradle/wrapper/gradle-wrapper.properties文件；3. 将distributionUrl指向本地的gradle-5.6-bin.zip路径，然后重新执行./gradlew shadowJar命令。

