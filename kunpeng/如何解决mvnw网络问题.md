# 如何解决mvnw网络问题

## 内核版本


## 问题现象
编译环境访问网络需要通过代理，导致使用mvnw编译时无法正常下载依赖。

## 问题根因
mvnw在自动下载Maven或依赖时未配置网络代理，而编译环境必须通过代理才能访问外网。

## 解决方案
编辑mvnw文件，在第227行添加代理参数："-Dhttp.proxyHost=127.0.0.1" "-Dhttp.proxyPort=3128" "-Dhttps.proxyHost=127.0.0.1" "-Dhttps.proxyPort=3128" \，其中IP和端口需根据实际代理环境调整，保存后重新执行编译命令 mvn clean install。

