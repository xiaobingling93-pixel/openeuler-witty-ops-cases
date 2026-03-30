# 启动OceanBase集群时提示open files must be not be less than 20000的解决方法

## 内核版本


## 问题现象
启动OceanBase集群时提示：open files must be not be less than 20000(Current value: 1024)。

## 问题根因
配置文件里面的最大文件数设置过小，导致打开文件数超过最大文件数时被阻止。

## 解决方案
1. 在服务器的命令行界面执行如下命令：
cat >> /etc/security/limits.conf << EOF 
*       soft    nofile  655350 
*       hard    nofile  655350 
EOF
2. 重新登录服务器，使配置生效。
3. 执行 ulimit -n 查看open files当前值，返回655350表示配置成功。

