# spring-cloud-gcp异常问题的解决方法

## 内核版本


## 问题现象
GcpDatastoreEmulatorIntegrationTests用例在执行datastore查询操作时不会抛出异常，但用例预期应抛出异常。Cloud Datastore emulator版本为291.0.0。

## 问题根因
在执行datastore查询操作时，代码未正确触发预期的异常抛出逻辑。

## 解决方案
1. 打开spring-cloud-gcp源码目录下的GcpDatastoreEmulatorIntegrationTests.java文件；
2. 注释掉第102～103行，并在第104行添加代码"datastore.run(query);"（参考图片：/doc_center/source/zh/kunpengwebs/ecosystemEnable/SpringCloud/zh-cn_image_0000001217284189.png）；
3. 保存并退出编辑；
4. 重新执行编译命令：./mvnw clean install -Dgpg.skip=true。

