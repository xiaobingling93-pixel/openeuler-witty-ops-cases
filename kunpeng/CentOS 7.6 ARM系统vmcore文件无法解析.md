# CentOS 7.6 ARM系统vmcore文件无法解析

## 内核版本
4.14.0-115.el7a.0.1.aarch64

## 问题现象
在CentOS 7.6系统 + RAID卡MR9560-8i环境中，内核crash生成的vmcore无法被正常解析，提示报错“crash: seek error: kernel virtual address: ffffa03ff7740090 type: \"IRQ stack pointer\"”。

## 问题根因


## 解决方案
1. 获取kexec-tools rpm包：
   cd /opt/
   mkdir kexec-tools && cd kexec-tools/
   wget https://archive.kernel.org/centos-vault/8.3.2011/BaseOS/aarch64/os/Packages/kexec-tools-2.0.20-34.el8.aarch64.rpm
   rpm2cpio kexec-tools-2.0.20-34.el8.aarch64.rpm | cpio -div
2. 替换makedumpfile：
   cp /opt/kexec-tools/usr/sbin/makedumpfile /usr/sbin/makedumpfile
3. 删除原有kdump.img：
   rm /boot/initramfs-4.14.0-115.el7a.0.1.aarch64kdump.img 
4. 重启kdump服务：
   systemctl restart kdump
5. 触发kdump：
   echo c > /proc/sysrq-trigger
6. 安装crash工具：
   yum install crash kernel-debuginfo*-`uname -r`
7. 重新启动调试：
   crash /usr/lib/debug/usr/lib/modules/4.14.0-115.el7a.0.1.aarch64/vmlinux /var/crash/127.0.0.1-xxxx/vmcore

