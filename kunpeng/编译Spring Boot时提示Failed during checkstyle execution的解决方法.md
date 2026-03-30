# 编译Spring Boot时提示Failed during checkstyle execution的解决方法

## 内核版本


## 问题现象
编译Spring Boot过程中，执行maven-checkstyle-plugin时失败，提示错误信息："[ERROR] Failed to execute goal org.apache.maven.plugins:maven-checkstyle-plugin:3.0.0:check (checkstyle-validation) on project spring-cloud-context: Failed during checkstyle execution: There is 1 error reported by Checkstyle 8.18 with checkstyle.xml ruleset."

## 问题根因
检查maven-checkstyle-plugin失败导致编译中断。该问题在x86架构环境中同样存在，且当前场景不涉及代码提交，因此可以安全移除该插件。

## 解决方案
1. 打开源码目录中的pom.xml文件；2. 使用<!--和-->注释掉maven-checkstyle-plugin所在的plugin配置；3. 保存并退出编辑；4. 重新执行编译命令：./mvnw clean install -Dgpg.skip=true。

