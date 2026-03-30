# 编译netty-tcnative-boringssl-static过程中告警exec returned: 1导致的编译失败

## 内核版本


## 问题现象
编译netty-tcnative-boringssl-static时出现错误：[ERROR] Failed to execute goal org.apache.maven.plugins:maven-antrun-plugin:1.8:run (build-boringssl) on project netty-tcnative-boringssl-static: An Ant BuildException has occurred: exec returned: 1，导致编译失败。

## 问题根因


## 解决方案
1. 删除openssl-dynamic/src/main/native-package/configure.ac文件中的-Werror编译参数，将${CFLAGS="-O3"} #${CFLAGS="-O3" -Werror}中的-Werror注释或移除。
2. 在openssl-dynamic/src/main/native-package/m4/apr_common.m4文件中，注释掉或删除dnl CFLAGS="$CFLAGS -Werror"这一行，避免启用-Werror。
3. 在boringssl-static/target/boringssl-chromium-stable/CMakeLists.txt文件中，清除CMAKE_C_FLAGS和CMAKE_CXX_FLAGS中的-Wshadow参数，设置为set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS}")和set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")。

