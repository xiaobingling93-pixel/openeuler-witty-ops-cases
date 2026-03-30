# openEuler系统下内存页Page Size如何从64K切换到4K？

## 内核版本
4.19

## 问题现象
openEuler 20.03系列操作系统默认内存页大小（Page Size）为64KB，但某些业务场景需要将其修改为4KB。

## 问题根因


## 解决方案
1. 使用getconf PAGESIZE确认当前页大小；2. 获取并解压对应内核源码；3. 配置本地Yum源并安装编译依赖；4. 使用make menuconfig进入内核配置界面，依次选择“Kernel Features” -> “Page size（64KB）”，将其修改为4KB；5. 确认.config中CONFIG_ARM64_4K_PAGES=y；6. 覆盖默认配置文件；7. 编译生成内核RPM包；8. 安装新内核并设置为默认启动项；9. 重启系统后验证Page Size是否变为4KB。

