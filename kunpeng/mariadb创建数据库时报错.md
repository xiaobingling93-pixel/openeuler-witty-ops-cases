# mariadb创建数据库时报错

## 内核版本


## 问题现象
Mariadb验证用户时正常，但在创建数据库时报错，错误信息为：“ERROR 1045 (28000): Access denied for user 'pasa'@'localhost' (using password: YES)”。

## 问题根因
pasa用户的权限配置存在问题，导致虽然能通过身份验证，但没有足够的权限执行创建数据库的操作。

## 解决方案
通过以下SQL命令手动为pasa用户插入权限记录：
mysql -upasa -p123456
use mysql;
insert into mysql.user(Host,User,Password) values("localhost","pasa",password("123456"));

