# 安装TensorFlow 2.6.5后，执行import tensorflow时报错

## 内核版本


## 问题现象
安装TensorFlow 2.6.5后，执行import tensorflow时报错：“RuntimeError: module compiled against API version 0x10 but this version of numpy is 0xd”。

## 问题根因
pip3安装TensorFlow时可能自动重装numpy，导致TensorFlow与当前numpy版本不兼容。

## 解决方案
执行命令卸载旧版本numpy，并安装TensorFlow 2.6.5适配的numpy 1.23.0版本：pip3 uninstall numpy && pip3 install numpy==1.23.0

