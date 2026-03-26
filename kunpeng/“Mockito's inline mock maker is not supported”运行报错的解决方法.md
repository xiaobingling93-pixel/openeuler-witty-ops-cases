# “Mockito's inline mock maker is not supported”运行报错的解决方法

## 内核版本


## 问题现象
运行测试用例失败，报错信息为“Mockito's inline mock maker is not supported”，如图所示：![](/doc_center/source/zh/kunpengdevps/userguide/Plugins_UserGuide/figure/zh-cn_image_0000002155346833.png)

## 问题根因
pom.xml文件未添加mockito-inline库。

## 解决方案
在pom.xml文件中添加mockito-inline库，具体依赖如下：
<dependency>
    <groupId>org.mockito</groupId>
    <artifactId>mockito-inline</artifactId>
    <version>3.9.0</version>
    <scope>test</scope>
</dependency>

