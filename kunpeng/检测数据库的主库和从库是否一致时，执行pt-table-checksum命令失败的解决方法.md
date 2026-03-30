# 检测数据库的主库和从库是否一致时，执行pt-table-checksum命令失败的解决方法

## 内核版本


## 问题现象
在检测MySQL主从数据库一致性时，执行pt-table-checksum命令失败。

## 问题根因
pt-table-checksum依赖的Perl模块DBD::mysql所使用的mysql.so动态链接库缺少对libmysqlclient.so.18的正确链接，导致无法正常加载所需MySQL客户端库。

## 解决方案
1. 定位libmysqlclient.so.18的实际路径（如/usr/lib64/mysql/）；2. 将该库文件复制到/usr/local/mysql/lib目录；3. 在/etc/ld.so.conf.d/mysql.conf中添加该路径并运行ldconfig更新动态链接库缓存；4. 验证mysql.so的依赖已正确解析；5. 重新执行pt-table-checksum命令即可成功运行。

