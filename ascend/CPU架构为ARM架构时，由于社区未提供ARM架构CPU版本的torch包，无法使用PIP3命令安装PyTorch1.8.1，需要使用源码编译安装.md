# CPU架构为ARM架构时，由于社区未提供ARM架构CPU版本的torch包，无法使用PIP3命令安装PyTorch1.8.1，需要使用源码编译安装

## 内核版本


## 问题现象
在ARM架构CPU环境下，无法通过pip3命令直接安装PyTorch 1.8.1。

## 问题根因
PyTorch官方社区未提供适用于ARM架构CPU的预编译torch包。

## 解决方案
需通过源码编译方式安装PyTorch 1.8.1。具体步骤包括：1）克隆PyTorch v1.8.1源码；2）初始化并更新子模块；3）设置环境变量USE_XNNPACK=0；4）执行python3 setup.py install进行编译安装。

