# 编译Spring Boot时提示UnknownHostException: fastdl.mongodb.org的解决方法

## 内核版本


## 问题现象
编译Spring Boot过程中，提示“java.net.UnknownHostException: fastdl.mongodb.org”。

## 问题根因
Host未建立映射关系，导致无法解析fastdl.mongodb.org域名。

## 解决方案
修改EmbeddedMongoAutoConfiguration.java源码：1. 在第43行下一行新增导入语句"import de.flapdoodle.embed.process.config.store.HttpProxyFactory;"；2. 将第220行代码修改为"IDownloadConfig downloadConfig = downloadConfigBuilder.proxyFactory(new HttpProxyFactory("127.0.0.1",3128)).build();"，其中127.0.0.1和3128需根据实际代理环境配置；3. 保存文件后重新编译Spring Boot。

