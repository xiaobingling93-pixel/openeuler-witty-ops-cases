# 编译Jansi时提示Failed to execute goal org.apache.maven.plugins:maven-javadoc-plugin

## 内核版本


## 问题现象
编译Jansi时出现错误：[ERROR] Failed to execute goal org.apache.maven.plugins:maven-javadoc-plugin:2.5:jar(attach-javadocs) on project jansi: MavenReportException: Error while creating archive: Exit code: 1，具体提示为Ansi.java文件中存在@param标签缺少描述的警告。

## 问题根因
Java 8引入了DocLint特性，在生成Javadoc时会严格检查注释格式。若注释不符合规范（如@param缺少描述），则Javadoc生成失败，导致Maven构建中断。

## 解决方案
在编译命令中添加参数跳过Javadoc检查：mvn clean package -Dmaven.javadoc.skip=true。

