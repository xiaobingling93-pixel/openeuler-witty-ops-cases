# 鲲鹏ARM架构可以安装Docker并部署K8s集群吗？

## 内核版本


## 问题现象
用户询问在鲲鹏ARM架构服务器上是否可以安装Docker并部署Kubernetes（K8s）集群。

## 问题根因
鲲鹏服务器基于ARM架构（aarch64），而部分用户可能尝试使用x86-64（amd64）架构的镜像或工具，导致兼容性问题。但Docker和K8s本身支持多架构，只要使用适配ARM架构的版本即可正常运行。

## 解决方案
支持在鲲鹏ARM架构上安装Docker并部署K8s集群。需确保使用aarch64架构的Docker和K8s镜像及安装包，具体操作可参考《Kubernetes 部署指南》和《Docker 安装指南（CentOS&openEuler）》。注意：鲲鹏服务器不支持amd64镜像，仅支持aarch64架构镜像。

