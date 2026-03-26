# 安装Python3后使用yum命令报错

## 内核版本


## 问题现象
安装Python3后使用yum命令时提示“ModuleNotFoundError: No module named 'dnf'”。

## 问题根因
openEuler系统自带python3.7，其yum命令是dnf的软链接，且与libpython3.7m.so.1.0强相关。当系统中安装了其他版本的Python3后，/usr/bin/python3可能指向了不兼容的Python版本，导致yum无法正确加载dnf模块。

## 解决方案
编辑/usr/bin/yum文件，将首行的#!/usr/bin/python3修改为#!/usr/bin/python3.7m，以确保yum使用系统自带的、与dnf兼容的Python3.7m解释器。具体步骤：1. 执行 vi /usr/bin/yum；2. 按i进入编辑模式，修改首行为#!/usr/bin/python3.7m；3. 按Esc键，输入:wq!保存并退出。

