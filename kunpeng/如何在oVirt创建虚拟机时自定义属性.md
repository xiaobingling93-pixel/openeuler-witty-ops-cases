# 如何在oVirt创建虚拟机时自定义属性

## 内核版本


## 问题现象
创建新的虚拟机时想要自定义属性qemu:commandline，但是自定义的属性不在关键字列表内。

## 问题根因
由于oVirt虚拟机的XML配置不支持手动修改，官方内置的自定义属性中没有qemu:commandline，但提供了vdsm-hook-qemucmdline扩展包支持，需要自行安装配置。

## 解决方案
1. 安装扩展包：yum install vdsm-hook-qemucmdline.noarch；2. 添加自定义属性配置：engine-config -s "UserDefinedVMProperties=qemu_cmdline=^.*$" --cver=4.4；3. 重启ovirt-engine服务：service ovirt-engine restart。之后在oVirt Web管理页面的“编辑虚拟机”->“自定义属性”中选择“qemu_cmdline”，并填写所需参数，例如：["-chardev","socket,path=/tmp/vm_sock0,server=on,wait=off,id=vm_sock","-device","virtio-serial","-device","virtserialport,chardev=vm_sock,name=serialport0"]。虚拟机启动后可通过virsh dumpxml命令验证配置是否生效。

