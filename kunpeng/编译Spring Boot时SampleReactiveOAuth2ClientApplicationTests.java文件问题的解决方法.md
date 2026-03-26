# 编译Spring Boot时SampleReactiveOAuth2ClientApplicationTests.java文件问题的解决方法

## 内核版本


## 问题现象
编译Spring Boot过程中需要访问“api.login.yahoo.com”，提示“UnknownHostException”。

## 问题根因
Host未建立映射关系，导致无法解析域名。

## 解决方案
1. 打开SampleReactiveOAuth2ClientApplicationTests.java文件。
2. 在第18行下面新增“import java.util.Properties;”。
3. 从第34行开始插入静态代码块，设置HTTP和HTTPS代理：
   static {
       Properties props = System.getProperties();
       props.put("http.proxyHost", "127.0.0.1");
       props.put("http.proxyPort", "3128");
       props.put("https.proxyHost", "127.0.0.1");
       props.put("https.proxyPort", "3128");
   }
   其中，127.0.0.1和3128分别表示代理主机的IP地址和端口，请根据实际代理环境配置。
4. 保存文件并重新编译Spring Boot。

