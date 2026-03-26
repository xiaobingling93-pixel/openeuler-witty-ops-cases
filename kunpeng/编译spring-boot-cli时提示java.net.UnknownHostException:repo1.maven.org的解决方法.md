# 编译spring-boot-cli时提示java.net.UnknownHostException:repo1.maven.org的解决方法

## 内核版本


## 问题现象
编译spring-boot-cli过程中遇到测试问题，提示“java.net.UnknownHostException:repo1.maven.org”。

## 问题根因
Host未建立映射关系，导致无法解析repo1.maven.org域名。

## 解决方案
在CompositeProxySelector.java文件中添加代理配置：导入java.util.Properties，并在static代码块中设置http和https代理主机为127.0.0.1、端口为3128（需根据实际代理环境调整）。注意使用Tab缩进，避免空格。

