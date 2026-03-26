# 编译Spring Boot时提示java.net.UnknownHostException的解决方法

## 内核版本


## 问题现象
编译Spring Boot过程中需要访问“self-signed.badssl.com”，提示“java.net.UnknownHostException”。

## 问题根因
Host未建立映射关系，导致无法解析域名。

## 解决方案
1. 打开ReactiveCloudFoundrySecurityService.java文件：vim ./spring-boot-project/spring-boot-actuator-autoconfigure/src/main/java/org/springframework/boot/actuate/autoconfigure/cloudfoundry/reactive/ReactiveCloudFoundrySecurityService.java
2. 在第27行下面新增：import reactor.netty.tcp.ProxyProvider;
3. 在第64行插入代理配置代码，设置HTTP代理（示例IP为127.0.0.1，端口为3128，需根据实际环境调整）。
4. 修改第77行为包含代理和SSL上下文的HttpClient创建代码，同样需配置正确的代理信息。
5. 保存文件并确保使用Tab缩进而非空格。
6. 重新编译Spring Boot。

