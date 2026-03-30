# 使用openssl req -new -x509命令生成证书失败

## 内核版本


## 问题现象
安装了鲲鹏加速引擎后使用openssl req -new -x509命令生成证书失败，提示“281461739307968:error:0E06D06C:configuration file routines:NCONF_get_string:no value:crypto/conf/conf_lib.c:273:group=req name=distinguished_name”。

## 问题根因
使用OpenSSL生成证书时会读取openssl.cnf配置文件，若安装了鲲鹏加速引擎并按指导文档以配置文件方式启用，则该自定义的openssl.cnf缺少生成证书所需的distinguished_name等必要配置项，导致命令执行失败。

## 解决方案
方法一：取消OPENSSL_CONF环境变量（unset OPENSSL_CONF），改用指定引擎路径方式（export OPENSSL_ENGINES="/usr/local/lib/engines-1.1"）。方法二：取消OPENSSL_CONF环境变量后，在OpenSSL自带的openssl.cnf文件中合适位置添加鲲鹏加速引擎配置段（包括openssl_conf=openssl_def、engine_section、kae_section等），保留原有证书生成所需配置，从而兼容KAE加速与证书生成功能。

