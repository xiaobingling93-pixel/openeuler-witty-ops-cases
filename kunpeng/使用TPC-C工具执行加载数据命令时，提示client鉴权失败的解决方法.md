# 使用TPC-C工具执行加载数据命令时，提示client鉴权失败的解决方法

## 内核版本


## 问题现象
使用TPC-C工具执行数据加载时，提示“client does not support authentication protocol requested by server;”。

## 问题根因
MySQL服务器要求的认证插件版本与客户端不匹配。

## 解决方案
将MySQL用户登录密码加密规则还原成mysql_native_password，并重置密码。具体操作为在数据库中执行以下语句：ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456'; ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '123456'; FLUSH PRIVILEGES; 然后重新执行加载数据命令。

