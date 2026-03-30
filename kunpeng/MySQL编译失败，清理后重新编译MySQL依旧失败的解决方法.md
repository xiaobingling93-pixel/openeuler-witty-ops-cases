# MySQL编译失败，清理后重新编译MySQL依旧失败的解决方法

## 内核版本


## 问题现象
MySQL编译失败，即使执行清理操作后重新编译仍然失败，报错提示“No such file or directory”。

## 问题根因
目录中存在之前编译MySQL时残留的相关文件，导致重新编译过程中出现路径或文件冲突，从而引发编译失败。

## 解决方案
1. 删除MySQL解压后的目录（例如：rm -rf mysql-8.0.25）；
2. 重新解压MySQL源码包（例如：tar -zxvf mysql-boost-8.0.17.tar.gz）；
3. 进入解压目录并重新执行编译安装步骤（包括创建build目录、cmake配置、make编译及install安装）。

