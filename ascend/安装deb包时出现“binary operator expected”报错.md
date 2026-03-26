# 安装deb包时出现“binary operator expected”报错

## 内核版本


## 问题现象
在Atlas系列多种硬件设备（如Atlas 300I Pro推理卡、Atlas 800训练服务器等）环境中安装deb包失败，终端报错“binary operator expected”。

## 问题根因
安装deb包时，会将其中的run包解压到当前运行环境的根目录“./”下。如果该目录下已存在相同版本的run包，则安装脚本会检测到两个安装包，导致条件判断语句语法错误，从而报出“binary operator expected”错误。

## 解决方案
移除当前根目录“./”下已存在的run包，然后重新执行deb包的安装操作。

