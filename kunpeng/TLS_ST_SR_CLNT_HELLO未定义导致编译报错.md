# TLS_ST_SR_CLNT_HELLO未定义导致编译报错

## 内核版本


## 问题现象
编译时提示TLS_ST_SR_CLNT_HELLO未定义，导致构建失败，错误信息为：Failed to execute goal org.fusesource hawtjni:maven-hawtjni-plugin:1.11:build (build-native-lib) on project netty-tcnative-boringssl-static: build failed: org.apache.maven.plugin.MojoExecutionException: make based build failed with exit code: 2。

## 问题根因


## 解决方案
1. 打开文件 openssl-dynamic/src/main/c/sslutils.c；2. 将代码中的 TLS_ST_SR_CLNT_HELLO 替换为数值 20（即修改为 if (state == 20)）；3. 保存并退出编辑，重新编译。

