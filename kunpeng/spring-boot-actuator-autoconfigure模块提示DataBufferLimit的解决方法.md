# spring-boot-actuator-autoconfigure模块提示DataBufferLimit的解决方法

## 内核版本


## 问题现象
编译过程中spring-boot-actuator-autoconfigure模块提示“DataBufferLimit”。

## 问题根因
由于spring-boot-actuator-autoconfigure模块缓冲字节超出限制。

## 解决方案
通过增加缓冲字节大小来解决。具体步骤：1. 打开WebMvcEndpointExposureIntegrationTests.java文件；2. 在第57行增加导入语句"import org.springframework.web.reactive.function.client.ExchangeStrategies;"；3. 修改第168行代码，使用ExchangeStrategies.builder()设置maxInMemorySize为512 * 1024，并将该策略应用到WebTestClient中；4. 保存并退出。注意使用Tab作为代码缩进，不能出现空格。

