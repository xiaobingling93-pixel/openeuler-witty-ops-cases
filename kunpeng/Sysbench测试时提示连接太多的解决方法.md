# Sysbench测试时提示连接太多的解决方法

## 内核版本


## 问题现象
服务器中安装了MySQL，使用Sysbench 1.0.5进行测试时，提示错误：FATAL: error 1040: Too many connections。

## 问题根因
数据库的连接数超过了配置参数设置的最大连接数。

## 解决方案
1. 修改数据库最大连接数，增加数据库连接数上限。可以在数据库中执行如下语句设置：set global max_connections = 3600; 2. 重新执行Sysbench测试操作。

