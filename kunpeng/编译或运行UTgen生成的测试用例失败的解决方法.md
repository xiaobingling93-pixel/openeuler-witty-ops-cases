# 编译或运行UTgen生成的测试用例失败的解决方法

## 内核版本


## 问题现象
当项目使用JDK 11及以上版本时，运行时出现“module java.base does not \"opens java.lang\" to unnamed module”报错信息。

## 问题根因
pom.xml文件或者build.gradle文件中未添加启动参数。

## 解决方案
在pom.xml文件或者build.gradle文件中添加编译启动参数。例如：在pom.xml文件中配置maven-compiler-plugin插件添加--add-exports参数，并在maven-surefire-plugin插件中通过argLine添加--add-opens参数，如：--add-opens java.base/java.lang=ALL-UNNAMED、--add-opens java.base/java.lang.reflect=ALL-UNNAMED、--add-opens java.desktop/sun.awt.util=ALL-UNNAMED。

