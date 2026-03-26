# 运行hdfs namenode -format时报错

## 内核版本


## 问题现象
运行hdfs namenode -format时报错，报错信息为：“Permission denied (publickey,gssapi-keyex,gssapi-with-mic,password)”。

## 问题根因
本机SSH免密登录配置有问题。

## 解决方案
使用ssh-keygen -t rsa命令重新生成SSH密钥对并配置免密登录。

