# 编译jline-2.14.3时提示下载doxia-module-apt-1.6.jar失败的解决方法

## 内核版本


## 问题现象
编译jline-2.14.3时提示下载doxia-module-apt-1.6.jar失败，错误信息为：Get request of: org/apache/maven/doxia-module-apt/1.6/doxia-module-apt-1.6.jar from huaweimaven failed。

## 问题根因


## 解决方案
手动下载相应的JAR包和pom文件到本地仓库中。执行以下命令：
wget https://repo1.maven.org/maven2/org/apache/maven/doxia/doxia-module-apt/1.6/doxia-module-apt-1.6.jar
wget https://repo1.maven.org/maven2/org/apache/maven/doxia/doxia-module-apt/1.6/doxia-module-apt-1.6.pom

