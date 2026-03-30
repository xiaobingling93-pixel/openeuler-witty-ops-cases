# ORCA不符合Greenplum版本要求导致Greenplum编译失败的解决方法

## 内核版本


## 问题现象
编译Greenplum 6.0.0过程中，提示“Your ORCA version is expected to be 3.74.XXX”。

## 问题根因
Greenplum和gporca版本兼容性问题。

## 解决方案
1. 确认Greenplum对gporca的版本要求：进入gpdb-6.0.0/depends目录，查看conanfile_orca.txt文件内容；2. 重新安装符合版本要求的gporca；3. 执行命令加载动态库：echo /usr/local/lib >/etc/ld.so.conf && ldconfig；4. 重新编译和安装Greenplum。

