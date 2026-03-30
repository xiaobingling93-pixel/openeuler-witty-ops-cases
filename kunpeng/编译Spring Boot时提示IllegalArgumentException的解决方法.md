# 编译Spring Boot时提示IllegalArgumentException的解决方法

## 内核版本


## 问题现象
用例执行过程中，提示“IllegalArgumentException ：this version does not support 32Bit”。

## 问题根因
编译过程中依赖的第三方包de.flapdoodle.embed.process-2.1.2.jar和de.flapdoodle.embed.mongo-2.2.0.jar并不支持ARM架构。

## 解决方案
1. 下载并适配支持ARM64架构的mongo和process两个JAR包：
   wget https://mirrors.huaweicloud.com/kunpeng/maven/de/flapdoodle/embed/de.flapdoodle.embed.mongo/2.2.0/de.flapdoodle.embed.mongo-2.2.0.jar
   wget https://mirrors.huaweicloud.com/kunpeng/maven/de/flapdoodle/embed/de.flapdoodle.embed.process/2.1.2/de.flapdoodle.embed.process-2.1.2.jar
2. 若缺少相关库目录，则需要先创建库目录：
   mkdir -p /root/.m2/repository/de/flapdoodle/embed/de.flapdoodle.embed.mongo/2.2.0
   mkdir -p /root/.m2/repository/de/flapdoodle/embed/de.flapdoodle.embed.process/2.1.2
3. 将下载的jar包移至相应目录下。
4. 以MongoDB 4.0.12版本为例，将测试用例中用到的其他版本替换掉：
   cd spring-boot-project/spring-boot-autoconfigure
   sed -i "s/3\.5\.5/4\.0\.12/g" `grep -rl "3\.5\.5"`
   sed -i "s/3\.4\.1/4\.0\.12/g" `grep -rl "3\.4\.1"`
   sed -i "s/3_4_15/4_0_12/g" `grep -rl "3_4_15"`
   cd ../../
5. 创建“/root/.embedmongo/extracted/Linux-B64--4.0.12”目录。
6. 参考《MongoDB 4.0.12 移植指南》中的MongoDB编译，编译MongoDB。
7. 将本地仓库目录下的MongoDB用编译成功后的MongoDB替换掉：
   \cp /usr/local/mongo/bin/mongod /root/.embedmongo/extracted/Linux-B64--4.0.12  && mv /root/.embedmongo/extracted/Linux-B64--4.0.12/mongod /root/.embedmongo/extracted/Linux-B64--4.0.12/extractmongod
8. 修改EmbeddedMongoAutoConfiguration.java文件，在第32行后添加import de.flapdoodle.embed.mongo.config.MongoCmdOptionsBuilder;，在第133行后添加代码：
   if (replSetName != null) {
       MongoCmdOptionsBuilder optionsBuilder = new MongoCmdOptionsBuilder();
       optionsBuilder.useNoJournal(false);
       builder.cmdOptions(optionsBuilder.build());
   }
注意：使用:set list检查格式，不能出现空格，请使用Tab作为代码缩进。

