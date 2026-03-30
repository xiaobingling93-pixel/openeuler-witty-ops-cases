# 驱动版本回退时出现“Device_image_crl_check failed”报错

## 内核版本


## 问题现象
在Atlas 300T训练卡（型号：9000）、Atlas 300T Pro训练卡（型号：9000）、Atlas 800训练服务器（型号：9000/9010）、Atlas 900计算节点、Atlas 900T RAK计算节点等产品环境中，将驱动从NPU 22.0.3版本直接回退至NPU 21.0.3及以下版本，或卸载NPU 22.0.3驱动后再安装NPU 21.0.3及以下版本时，出现“Device_image_crl_check failed”报错，导致驱动安装失败。

## 问题根因
crl文件校验失败。

## 解决方案
先安装NPU 21.0.4驱动版本，再安装NPU 21.0.3及以下驱动版本。

