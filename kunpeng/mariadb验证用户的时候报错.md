# mariadb验证用户的时候报错

## 内核版本


## 问题现象
Mariadb验证用户时报错，报错信息类似：“ERROR 1045 (28000): Access denied for user 'test'@'localhost' (using password: YES)”。

## 问题根因
默认的plugin属性有问题。

## 解决方案
执行以下命令，修改plugin属性：
update user set authentication_string=PASSWORD(''), plugin='mysql_native_password' where user='root';
flush privileges;

