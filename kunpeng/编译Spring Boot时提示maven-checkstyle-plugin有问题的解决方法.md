# 编译Spring Boot时提示maven-checkstyle-plugin有问题的解决方法

## 内核版本


## 问题现象
编译Spring Boot过程中由于检查maven-checkstyle-plugin，提示错误信息：[ERROR] Failed to execute goal org.apache.maven.plugins:maven-checkstyle-plugin:3.0.0:check(checkstyle-validation) on project spring-cloud-gateway-core: Failed during checkstyle execution: There are 47 errors reported by Checkstyle 8.18 with checkstyle.xml ruleset.

## 问题根因
在x86架构环境中，maven-checkstyle-plugin插件的检查会失败。由于该案例不涉及代码提交，该插件的检查并非必需，因此其存在导致编译中断。

## 解决方案
将pom.xml文件中maven-checkstyle-plugin插件部分的代码注释掉：1. 打开pom.xml；2. 在插件定义的开始位置（第31行后）插入<!--，在结束位置（第89行后）插入-->；3. 保存文件并重新执行编译命令 mvn clean install -Dgpg.skip=true。

