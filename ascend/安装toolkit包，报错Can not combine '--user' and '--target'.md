# 安装toolkit包，报错Can not combine '--user' and '--target'

## 内核版本


## 问题现象
安装toolkit包时报错：ERROR: Can not combine '--user' and '--target'。

## 问题根因
pip配置文件中同时启用了--user和--target选项，导致pip install命令冲突。

## 解决方案
1. 执行vim ~/.pip/pip.conf命令打开pip配置文件；2. 将配置修改为user = false；3. 保存并退出；4. 重新执行CANN安装操作。

