# Spring-boot-gradle-plugin编译依赖拉取问题的解决方法

## 内核版本


## 问题现象
编译Spring Boot过程中需要访问“repo.maven.apache.org”，提示“UnknownHostException”。

## 问题根因
Host未建立映射关系，导致无法解析域名。

## 解决方案
通过在GradleBuild.java文件中增加代理配置解决：1. 在指定位置插入代理参数（-Dhttp.proxyHost、-Dhttp.proxyPort、-Dhttps.proxyHost、-Dhttps.proxyPort）；2. 修改相应代码行以使用新参数；3. 保存并重新编译。注意使用Tab缩进，避免空格。

