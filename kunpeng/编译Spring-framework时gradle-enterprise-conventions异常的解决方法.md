# 编译Spring-framework时gradle-enterprise-conventions异常的解决方法

## 内核版本


## 问题现象
编译Spring Framework时出现gradle-enterprise-conventions插件解析异常，提示“Error resolving plugin [id: 'io.spring.gradle-enterprise-conventions', version: '0.0.2']”。

## 问题根因
Gradle在构建过程中无法解析指定的插件'io.spring.gradle-enterprise-conventions'版本'0.0.2'，可能是由于该插件在当前构建环境中不可用或未正确配置插件仓库。

## 解决方案
1. 打开build.gradle文件；
2. 将第6行内容注释掉：//id 'io.spring.gradle-enterprise-conventions' version '0.0.2'；
3. 保存并退出编辑；
4. 重新编译Spring Framework。
参考图示：![](/doc_center/source/zh/kunpengwebs/ecosystemEnable/SpringFramework/zh-cn_image_0000001322209841.png)

