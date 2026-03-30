# fio测试时远程客户端连接失败的解决方法

## 内核版本


## 问题现象
执行fio测试时，提示无法连接远程客户端，错误信息为：fio: connect: Connection refused；fio: failed to connect to 192.168.3.132:8765。

## 问题根因
远程客户端fio服务未启动。

## 解决方案
1. 使用命令 ps -ef | grep fio 检查发现远程客户端fio服务未启动；2. 在远程客户端上执行 fio --server 启动fio服务；3. 重新下发fio测试命令。

