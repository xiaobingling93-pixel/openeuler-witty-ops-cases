# Percona数据库中安装TokuDB引擎失败的解决方法

## 内核版本


## 问题现象
在鲲鹏服务器CentOS 7.6环境下，安装Percona数据库的TokuDB引擎时失败，报错提示无法找到libjemalloc.so.1库文件："ERROR: Cannot find libjemalloc.so.1 library. Make sure you have libjemalloc1 on debian|ubuntu or jemalloc on centos package installed."

## 问题根因
问题并非由jemalloc库版本（如libjemalloc.so.1或libjemalloc.so.2）引起，而是因为TokuDB在编译时会读取jemalloc源码包中的“VERSION”文件以判断版本。从网上下载的jemalloc源码包在执行autogen.sh后生成的“VERSION”文件内容为全0，导致TokuDB误判版本低于2.3.0，从而拒绝加载。

## 解决方案
1. 删除已有的jemalloc库文件（如libjemalloc.so.1和libjemalloc.so.2）；
2. 在jemalloc源码目录中手动创建“VERSION”文件，并写入有效版本字符串，例如："5.2.1-0-g0000000000000000000000000000000000000000"；
3. 重新执行编译安装命令：./autogen.sh && ./configure && make && make install；
4. 再次在Percona中执行INSTALL PLUGIN tokudb SONAME 'ha_tokudb.so'; 安装TokuDB引擎；
5. 通过show engines; 验证TokuDB是否成功加载。

