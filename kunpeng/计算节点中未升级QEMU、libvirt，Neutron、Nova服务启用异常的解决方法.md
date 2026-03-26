# 计算节点中未升级QEMU、libvirt，Neutron、Nova服务启用异常的解决方法

## 内核版本


## 问题现象
在部署vKAE特性时，虚拟机部署Nginx过程中生成OpenSSL证书时报错，同时Neutron、Nova服务启用异常。

## 问题根因
计算节点中未升级QEMU和libvirt组件，导致与vKAE特性不兼容，从而引发Neutron、Nova服务异常以及OpenSSL证书生成失败。

## 解决方案
升级计算节点上的QEMU和libvirt至与vKAE特性兼容的版本，确保Neutron和Nova服务正常启用，并支持虚拟机中OpenSSL证书的正确生成。

