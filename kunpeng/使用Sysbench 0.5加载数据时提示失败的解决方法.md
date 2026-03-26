# 使用Sysbench 0.5加载数据时提示失败的解决方法

## 内核版本


## 问题现象
使用Sysbench 0.5版本测试工具测试MySQL数据库时，在加载数据过程中提示以下错误：FATAL: unable to connect to MySQL server, aborting... FATAL: error 2026: SSL connection error: SSL_CTX_set_tmp_dh failed FATAL: failed to execute function 'prepare': /home/sysbench-0.5/sysbench/tests/db/common.lua: 103: Failed to connect to the database。

## 问题根因
Sysbench二进制文件与libcrypto、libssl库的版本不匹配。

## 解决方案
在本机上升级libcrypto、libssl库到较新的版本，并重新编译Sysbench。

