# 升级openEuler系统的OpenSSL版本到1.1.1e，导致SSH连接不上

## 内核版本


## 问题现象
升级openEuler 20.03 LTS系统的OpenSSL版本到1.1.1e后，SSH连接失败。

## 问题根因
OpenSSL工具自带的默认openssl.cnf文件没有生效，可能是因为人为修改了该文件的名称，导致SSH服务无法正常加载配置。

## 解决方案
解决方案包括两种方式：方式一，直接使用系统自带的OpenSSL 1.1.1d版本，安装openssl-devel并按照《鲲鹏加速引擎 用户指南》进行KAE环境安装；方式二，升级到OpenSSL 1.1.1e，需完成以下步骤：(1) 下载并编译安装OpenSSL 1.1.1e；(2) 配置环境变量和软链接；(3) 更新动态链接库；(4) 安装KAEdriver、KAE和KAEzip，并确保在configure时指定新OpenSSL路径；(5) 验证安装成功。同时，应确保openssl.cnf文件存在且未被重命名，可通过find / -name "openssl.cnf"检查。

