# 在x86服务器上部署MySQL主从复制时提示无法验证身份的解决方法

## 内核版本


## 问题现象
在x86服务器上部署MySQL主从复制时，执行 start slave; 命令后报错：Authentication plugin 'caching_sha2_password' reported error: Authentication requires secure connection. Error_code: MY-002061。

## 问题根因
当前客户端没有保存服务端的RSA公钥文件，导致服务端无法验证身份。

## 解决方案
1. 执行 stop slave; 停止主从复制；2. 在 change master 命令中添加 get_master_public_key=1 参数，例如：change master to master_host='192.168.0.1',master_port=3306,master_user='replicate',master_password='123456',master_auto_position=1,get_master_public_key=1; 3. 执行 start slave; 重新启动复制，并通过 show slave status\G; 检查复制状态。

