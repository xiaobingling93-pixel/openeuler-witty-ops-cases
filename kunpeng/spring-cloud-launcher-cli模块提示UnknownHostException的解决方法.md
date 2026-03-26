# spring-cloud-launcher-cli模块提示UnknownHostException的解决方法

## 内核版本


## 问题现象
编译Spring-Cloud-cli过程中spring-cloud-launcher-cli模块编译失败，提示“UnknownHostException”。

## 问题根因
主机未建立映射关系，导致无法解析主机名。

## 解决方案
1. 打开LauncherCommand.java文件：vim /home/spring-cloud-cli/spring-cloud-launcher/spring-cloud-launcher-cli/src/main/java/org/springframework/cloud/launcher/cli/LauncherCommand.java
2. 在第22行的下一行添加：import java.util.Properties;
3. 在第52行的下一行添加静态代码块，配置代理：
   static {
       Properties props = System.getProperties();
       props.put("http.proxyHost", "127.0.0.1");
       props.put("http.proxyPort", "3128");
       props.put("https.proxyHost", "127.0.0.1");
       props.put("https.proxyPort", "3128");
   }
   其中，127.0.0.1和3128分别表示代理主机的IP地址和端口，请根据实际代理环境配置。注意使用Tab作为代码缩进，不能出现空格。
4. 保存并退出编辑。
5. 重新执行编译命令：./mvnw clean install -Dgpg.skip=true

