# 执行virt-install创建虚拟机时提示“ERROR Cannot access storage file 'xxxxx' (as uid:107, gid:107): Permission denied”

## 内核版本


## 问题现象
执行virt-install创建虚拟机时，系统报错“ERROR Cannot access storage file '/home/kvm/images/openeuler.img' (as uid:107, gid:107): Permission denied”，原因是libvirt默认以qemu用户（uid:107, gid:107）运行，而该用户对存储文件所在目录无访问权限。

## 问题根因
libvirt的qemu进程默认以非root用户（如qemu，uid:107）运行，而虚拟机磁盘镜像文件或其上级目录（如/home/kvm）未授予该用户足够的读写或搜索权限，导致无法访问存储文件。

## 解决方案
修改/etc/libvirt/qemu.conf配置文件，取消注释并设置user和group为root：执行sed -i 's/#user = "root"/user = "root"/g' /etc/libvirt/qemu.conf 和 sed -i 's/#group = "root"/group = "root"/g' /etc/libvirt/qemu.conf，然后重启libvirtd服务（service libvirtd restart）。

