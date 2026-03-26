# 编译HBase-shaded-netty时提示Failed to apply patch: HBASE-15789_v2.path的解决方法

## 内核版本


## 问题现象
编译HBase-shaded-netty时提示Failed to apply patch: HBASE-15789_v2.path，具体错误信息为：[ERROR] Failed to execute goal org.apache.maven.plugins:maven-patch-plugin:1.2:apply (patch) on project hbase-shaded-protobuf: Failed to apply patch: HBASE-15789_v2.path. See debug output for more information. Error while executing process. Cannot run program "patch"

## 问题根因
系统缺少patch工具，导致Maven无法执行打补丁操作。

## 解决方案
执行命令手动安装patch工具：yum -y install patch

