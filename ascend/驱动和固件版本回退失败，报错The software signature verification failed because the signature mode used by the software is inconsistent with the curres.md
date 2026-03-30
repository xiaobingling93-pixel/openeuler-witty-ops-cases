# 驱动和固件版本回退失败，报错The software signature verification failed because the signature mode used by the software is inconsistent with the curres

## 内核版本


## 问题现象
在驱动和固件版本回退过程中，系统报错：'The software signature verification failed because the signature mode used by the software is inconsistent with the curres'，导致回退操作失败。

## 问题根因
PKCS签名校验失败，软件使用的签名模式与当前系统要求的签名模式不一致。

## 解决方案
1. 安装NPU 22.0.3及以上版本的驱动和配套固件；2. 执行命令 'npu-smi set -t pkcs-enable -d 0' 使能PKCS状态；3. 使能后按照固件→驱动的顺序重新执行版本回退操作。

