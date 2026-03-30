# spring-cloud-gateway异常问题的解决方法

## 内核版本


## 问题现象
编译安装过程中，由于编译环境网络较差，导致spring-cloud-gateway出现异常。

## 问题根因
环境网络较差，导致请求超时或失败，从而引发spring-cloud-gateway异常。

## 解决方案
1. 编辑RetryGatewayFilterFactoryIntegrationTests.java文件；2. 适当延长timeout（如CentOS 7.6/openEuler 20.03设为30s，CentOS 8.1设为100s）并增加重试次数（推荐5次），具体修改如下：
"spring.cloud.gateway.httpclient.response-timeout=30s",
"spring.cloud.spring.cloud.routes.filters.args.retries=5"；3. 保存文件后重新执行编译命令：./mvnw clean install -Dgpg.skip=true。

