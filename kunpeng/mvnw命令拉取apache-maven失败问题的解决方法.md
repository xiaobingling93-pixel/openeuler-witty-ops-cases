# mvnw命令拉取apache-maven失败问题的解决方法

## 内核版本


## 问题现象
如果编译环境通过代理访问互联网，在编译时可能会遇到无法下载apache-maven-3.5.0-bin.zip压缩文件的问题。

## 问题根因
编译环境通过代理访问互联网，导致编译时无法下载压缩文件。

## 解决方案
在mvnw脚本文件中添加代理配置：打开mvnw文件，进入编辑模式，添加"-Dhttp.proxyHost=127.0.0.1" "-Dhttp.proxyPort=3128" "-Dhttps.proxyHost=127.0.0.1" "-Dhttps.proxyPort=3128" \（其中IP和端口需根据实际代理环境修改），保存后重新执行mvnw命令（如：./mvnw clean install -Dgpg.skip=true）。

