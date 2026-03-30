# 测试KAE解压缩性能时提示没有权限获取相关设备资源的解决办法

## 内核版本


## 问题现象
完成KAE的安装部署后，测试KAE解压缩性能时提示无法打开“/dev”路径下的相关字符设备，报错信息为：“open /dev/hisi_zip-5 failed, errno = 13!”。

## 问题根因
只有root用户对“/dev”下hisi前缀的设备具有读写权限，普通用户在运行KAE性能测试程序时因缺少权限而无法打开相关字符设备。

## 解决方案
1. 创建kaegroup用户组，将设备文件添加到该用户组，更改设备文件权限，并让需要使用KAE的用户加入该组：
   groupadd kaegroup
   chown :kaegroup /dev/hisi_*
   chmod 660 /dev/hisi_*
   usermod -aG kaegroup KAE用户名
2. 验证设备权限是否已正确设置。
3. 重新执行性能测试命令（如：./kaezip_perf -m 8 -l 10240 -n 1000）。

