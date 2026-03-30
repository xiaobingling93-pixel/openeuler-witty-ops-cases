# PyTorch框架模型训练迁移时报错“Stream mode cannot be set in current driver version”

## 内核版本


## 问题现象
在AICC上迁移PyTorch框架模型在NPU上训练时，驱动层报错“Stream mode cannot be set in current driver version”。硬件配置为CANN版本6.3.RC1、Driver版本5.1.RC1、Torch版本1.8.1。

## 问题根因
c84版本引入了一个遇错即停的特性，该功能需CANN和驱动包均为c84以上版本才能生效。但PyTorch包默认启用了该功能，而当前驱动版本低于c84，导致报错（但不影响业务和功能）。

## 解决方案
升级driver版本至C84或更高版本。

