# DevKit Pipeline如何安装毕昇JDK 21？

## 内核版本


## 问题现象
DevKit Pipeline不支持批量安装毕昇JDK 21。

## 问题根因
DevKit Pipeline仅支持批量安装毕昇JDK 8和毕昇JDK 17，未提供对毕昇JDK 21的批量安装支持。

## 解决方案
若需要安装毕昇JDK 21，可通过以下两种方式：1. 单独安装：下载毕昇JDK安装包，在服务器上进行安装；2. 批量安装：参考批量安装毕昇JDK文档，获取并使用四个脚本文件（update_to_bisheng_jdk_in_batchs.sh、unpack_and_modify.sh、ip.all、check_java_home_and_path_in_batch.sh）进行配置和批量安装。

