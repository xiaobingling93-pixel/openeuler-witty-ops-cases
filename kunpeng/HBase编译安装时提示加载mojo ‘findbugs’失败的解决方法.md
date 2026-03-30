# HBase编译安装时提示加载mojo ‘findbugs’失败的解决方法

## 内核版本


## 问题现象
在HBase编译安装过程中提示加载mojo 'findbugs'失败，导致默认的findbugs-maven-plugin执行中断，错误信息为：Failed to execute goal org.codehaus.mojo:findbugs-maven-plugin:3.0.0:findbugs(default) on project hbase: Execution default of goal org.codehaus.mojo:findbugs-maven Failed: Unable to load the mojo 'findbugs' in the plugin 'org.codehaus.mojo:findbugs-maven-plugin:3.0.0'

## 问题根因
findbugs-maven-plugin组件版本不正确。

## 解决方案
1. 打开“pom.xml”文件（vi pom.xml）；2. 进入编辑模式，将findbugs-maven-plugin的版本修改为3.0.4，即设置<groupId>org.codehaus.mojo</groupId><artifactId>findbugs-maven-plugin</artifactId><version>3.0.4</version>；3. 保存并退出编辑（Esc后输入:wq!）。

