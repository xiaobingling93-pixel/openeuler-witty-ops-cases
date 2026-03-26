# 重启Nginx服务失败的解决方法

## 内核版本


## 问题现象
修改nginx.conf文件后，重启Nginx服务失败，提示“No such file or directory:fopen('/home/nginx/dhparam.pem','r') error:200...”。

## 问题根因
启动Nginx时，缺少dhparam.pem文件。

## 解决方案
1. 生成dhparam.pem文件：执行命令 openssl dhparam -dsaparam -out dhparam.pem 4096；2. 重启Nginx服务：执行命令 sbin/nginx -s reload。

