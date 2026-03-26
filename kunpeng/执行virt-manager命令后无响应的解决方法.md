# 执行virt-manager命令后无响应的解决方法

## 内核版本


## 问题现象
执行virt-manager命令启动qemu-kvm图形管理界面时，没有任何反应，也没有提示任何信息。

## 问题根因
系统之前编译安装过zlib源码，导致GTK在加载图标文件时因PNG图像读取错误而失败，具体错误为：Failed to load /usr/share/icons/Adwaita/24x24/status/image-missing.png: Fatal error reading PNG image file。

## 解决方案
进入zlib编译安装目录，执行make uninstall卸载自行编译安装的zlib，然后重新运行virt-manager命令即可恢复正常。

