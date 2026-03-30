# Tomcat多用户请求连接超时的解决方法

## 内核版本


## 问题现象
在CentOS 7.6、MySQL 5.7.26、Tomcat 8.5.32环境下，使用LoadRunner进行压力测试时，当并发用户连接数超过3个，出现连接失败，错误提示为“Failed to connect to server '128.5.69.44:8082': [10048] Address already in use”。

## 问题根因
负载生成器发送数据包速度过快，导致服务器端口在TIME_WAIT状态未释放前被迅速占满，造成端口资源耗尽。

## 解决方案
1. 在LoadRunner中修改运行时设置（Run Time Settings）：将HTTP-request connect timeout、HTTP-request receive timeout、Step download timeout分别设为1000、1000、10000；
2. 取消勾选Browser Emulation中的“Download non-HTML resources”选项；
3. 在“Runtime Setting”>“Internet Protocol：Preferences”>“Advanced”中勾选“wininet replay instead of sockets”；
4. 重新执行多用户连接测试。

