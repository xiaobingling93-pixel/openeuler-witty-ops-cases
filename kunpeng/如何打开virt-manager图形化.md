# 如何打开virt-manager图形化

## 内核版本


## 问题现象
启动Virtual Machine Manager时提示“Error polling connection 'qemu:///system': internal error: Socket 6378 can't be handled (max socket is 4095)”。

## 问题根因
libvirt-4.5.0代码bug导致的问题。

## 解决方案
升级libvirt版本至libvirt-4.7.0以上，或者修改libvirt-4.5.0源码后重新编译。以升级至libvirt-5.6.0为例：1. 安装依赖包（yum -y install yum-utils rpm-build）；2. 下载源码RPM包（wget https://libvirt.org/sources/libvirt-5.6.0-1.fc30.src.rpm）；3. 编译安装：a. 安装src.rpm源码包（rpm -i libvirt-5.6.0-1.fc30.src.rpm），b. 生成RPM包（cd /root/rpmbuild/SPECS/; yum-builddep -y libvirt.spec; rpmbuild -ba libvirt.spec），c. 安装RPM包（cd /root/rpmbuild/RPMS/aarch64/; yum -y install *.rpm），d. 重启libvirtd服务（systemctl daemon-reload; systemctl restart libvirtd）。

