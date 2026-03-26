# 编译安装Spring Boot过程中提示ModifiedClassPathExtensionOverridesTests的解决方法

## 内核版本


## 问题现象
编译安装Spring Boot过程中，编译环境通过代理访问外网，会遇到“ModifiedClassPathExtensionOverridesTests”测试失败的问题。

## 问题根因
注解ClassPathOverrides没有正常拉取到依赖导致的问题。

## 解决方案
1. 打开ModifiedClassPathClassLoader.java文件：vim ./spring-boot-project/spring-boot-tools/spring-boot-test-support/src/main/java/org/springframework/boot/testsupport/classpath/ModifiedClassPathClassLoader.java
2. 在第42行的下一行增加代码：import org.eclipse.aether.repository.Proxy;
3. 修改第202-203行内容，将原有的CollectRequest构造方式替换为通过RemoteRepository.Builder设置代理的方式，例如：
   RemoteRepository.Builder builder = new RemoteRepository.Builder("central", "default","https://repo.maven.apache.org/maven2");
   RemoteRepository remoteRepository = builder.setProxy(new Proxy("https", "127.0.0.1", 3128)).build();
   CollectRequest collectRequest = new CollectRequest(null, Arrays.asList(remoteRepository));
   其中，127.0.0.1和3128分别表示代理主机的IP地址和端口，需根据实际代理环境配置。
4. 保存并退出编辑。
5. 重新执行编译命令：mvn spring-javaformat:apply clean install

