# 将数据导入MySQL时出现无效终端数问题的解决方法

## 内核版本


## 问题现象
将数据导入MySQL时出现无效终端数量问题，并提示“invalid number of terminals”。

## 问题根因
JDBC Connector发出的连接请求超过了MySQL服务端配置的最大连接数限制。

## 解决方案
1. 在MySQL客户端执行SQL语句 'show variables like "max_connections";' 查看最大连接数。
2. 修改my_mysql.properties文件中的“terminals”值，确保其小于“max_connections”的值：
   a. 使用命令 'vi my_mysql.properties' 打开文件；
   b. 按“i”进入编辑模式，修改“terminals”为合适值（参考示例图片：/doc_center/source/zh/kunpengdbs/ecosystemEnable/MySQL/zh-cn_image_0000002045174289.png）；
   c. 按“Esc”，输入:wq!保存退出。
3. 重新执行数据加载命令 './runDatabaseBuild.sh my_mysql.properties'。

