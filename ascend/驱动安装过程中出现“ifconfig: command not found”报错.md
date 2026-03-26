# 驱动安装过程中出现“ifconfig: command not found”报错

## 内核版本


## 问题现象
Atlas 200I A2 加速模块环境驱动安装过程中提示“ifconfig: command not found”报错。

## 问题根因
系统未安装net-tools工具。

## 解决方案
1. 执行命令 apt-get install net-tools 安装net-tools工具；2. 执行ifconfig命令验证是否安装成功，若能正常显示网络接口信息则说明安装成功。

