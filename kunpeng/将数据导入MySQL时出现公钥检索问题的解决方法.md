# 将数据导入MySQL时出现公钥检索问题的解决方法

## 内核版本


## 问题现象
将数据导入MySQL时出现公钥检索问题，并提示“Public Key Retrieval is not allowed”。

## 问题根因
当MySQL 8.0使用caching_sha2_password插件进行身份验证时，需要使用公钥进行加密，MySQL客户端（例如Connector）需要能够检索该公钥。如果客户端未正确配置以允许公钥检索，将导致该问题。

## 解决方案
配置客户端连接选项，启用公钥检索：1. 打开my_mysql.properties文件；2. 为文件中的“jdbc”配置添加参数 allowPublicKeyRetrieval=true；3. 保存并退出编辑；4. 重新执行加载数据命令 ./runDatabaseBuild.sh my_mysql.properties。

