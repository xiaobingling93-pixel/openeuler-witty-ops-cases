# 创建Ubuntu22.04虚拟机，进入虚拟机后安装驱动报错

## 内核版本


## 问题现象
在Ubuntu 22.04虚拟机中安装驱动时出现报错，错误信息显示与Secure Boot相关，驱动无法正常安装。

## 问题根因
Ubuntu系统在启用UEFI Secure Boot的情况下，会阻止安装未经签名的第三方驱动程序，导致驱动安装失败。

## 解决方案
进入虚拟机的BIOS界面关闭Secure Boot：通过virsh console连接虚拟机，在UEFI Shell中输入exit进入BIOS；依次选择Device Manager > Secure Boot Configuration > Attempt Secure Boot，将其禁用；然后选择Reset Secure Boot Keys并确认；最后重启虚拟机使设置生效。

