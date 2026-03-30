# spring-boot-autoconfigure模块ElasticSearch测试问题的解决方法

## 内核版本


## 问题现象
ElasticSearch测试中使用了注解@Testcontainers(disabledWithoutDocker = true)来检测环境是否支持Docker。如果支持Docker，则执行该用例；如果不支持，则跳过该用例。

## 问题根因
编译环境已经安装并启动了Docker，导致测试用例被触发执行，可能引发非预期的测试行为或失败。

## 解决方案
1. 执行命令 systemctl stop docker 关闭Docker服务。
2. 关闭Docker服务后，再次进行ElasticSearch测试。

