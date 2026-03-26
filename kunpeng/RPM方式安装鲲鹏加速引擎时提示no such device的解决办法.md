# RPM方式安装鲲鹏加速引擎时提示no such device的解决办法

## 内核版本


## 问题现象
在使用RPM方式安装鲲鹏加速引擎时，报“no such device”错误，具体错误信息：“modprobe: ERROR: could not insert 'hisi_rde': No such device”。

## 问题根因
鲲鹏加速引擎的硬件设备没有被使能，即没有正确安装有效的License。

## 解决方案
正确安装有效的License。License的获取和安装步骤请参见《鲲鹏加速引擎 用户指南》中“环境部署”章节的“获取License”部分。

