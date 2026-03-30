# spring-cloud-cli异常问题timeout的解决方法

## 内核版本


## 问题现象
编译时遇到spring-cloud-cli-integration-tests报错，具体表现为测试超时失败。

## 问题根因
环境网络较差，导致集成测试在默认timeout时间内无法完成。

## 解决方案
修改CliTester.java文件中SampleIntegrationTests的timeout参数：CentOS 7.6/openEuler 20.03将6min改为20min，CentOS 8.1将6min改为30min，然后重新执行编译命令 ./mvnw clean install -Dgpg.skip=true。

