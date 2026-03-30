# Atlas 800-3010 Ubuntu系统配置kdump触发crash卡死

## 内核版本
4.15.0-34-generic

## 问题现象
Ubuntu系统配置kdump后，系统crash会卡死，无法正常生成内存转储。

## 问题根因
crashkernel默认配置的预留内存大小为128M，对于64G内存的服务器来说太小，导致kdump无法正常工作。

## 解决方案
在/etc/default/grub.d/kdump-tools.cfg中配置更大的预留内存，例如添加GRUB_CMDLINE_LINUX_DEFAULT="$GRUB_CMDLINE_LINUX_DEFAULT crashkernel=384M-:512M"，然后执行sudo update-grub并重启系统。

