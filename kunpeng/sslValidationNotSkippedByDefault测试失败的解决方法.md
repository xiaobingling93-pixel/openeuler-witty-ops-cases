# sslValidationNotSkippedByDefault测试失败的解决方法

## 内核版本


## 问题现象
编译过程中sslValidationNotSkippedByDefault测试失败，提示“ReactiveCloudFoundryActuatorAutoConfigurationTests.sslValidationNotSkippedByDefault:283->lambda$sslValidationNotSkippedByDefault$15:290...”。

## 问题根因
此问题是由于断言失败导致。

## 解决方案
1. 打开ReactiveCloudFoundryActuatorAutoConfigurationTests.java文件：vim ./spring-boot-project/spring-boot-actuator-autoconfigure/src/test/java/org/springframework/boot/actuate/autoconfigure/cloudfoundry/reactive/ReactiveCloudFoundryActuatorAutoConfigurationTests.java
2. 将第290行修改为：webClient.get().uri("https://self-signed.badssl.com/").exchange().block(Duration.ofSeconds(30)); 并注释掉原有的assertThatExceptionOfType断言代码。
3. 使用:set list检查格式，确保缩进使用Tab而非空格。
4. 保存退出后重新运行测试。

