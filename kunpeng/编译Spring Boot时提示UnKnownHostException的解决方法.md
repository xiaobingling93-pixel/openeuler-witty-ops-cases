# 编译Spring Boot时提示UnKnownHostException的解决方法

## 内核版本


## 问题现象
编译Spring Boot过程中需要访问“www.liquibase.org”，但提示“UnknownHostException”错误。

## 问题根因
Host未建立映射关系，导致无法解析域名“www.liquibase.org”。

## 解决方案
1. 打开LiquibaseAutoConfigurationTests.java文件：vim ./spring-boot-project/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/liquibase/LiquibaseAutoConfigurationTests.java
2. 在第24行下一行新增：import java.util.Properties;
3. 在第76行插入静态代码块，设置代理配置：
   static {
       Properties props = System.getProperties();
       props.put("http.proxyHost", "127.0.0.1");
       props.put("http.proxyPort", "3128");
       props.put("https.proxyHost", "127.0.0.1");
       props.put("https.proxyPort", "3128");
   }
   其中，127.0.0.1和3128为代理主机IP和端口，请根据实际环境修改。
4. 保存并退出编辑（:wq!）。
5. 重新编译Spring Boot。
注意：使用:set list检查格式，确保缩进使用Tab而非空格。

