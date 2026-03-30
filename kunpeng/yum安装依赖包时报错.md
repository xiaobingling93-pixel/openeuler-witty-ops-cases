# yum安装依赖包时报错

## 内核版本


## 问题现象
在openEuler环境下使用yum安装依赖包时出现错误，具体错误信息见截图：![](/doc_center/source/zh/kunpenghpcs/hpcindapp/trouble/zh-cn_image_0000001251772607.png)

## 问题根因
系统缺少所需的依赖库文件，导致yum无法自动解析并安装相关依赖。

## 解决方案
根据报错提示，手动下载并安装以下RPM包：
- gsl: wget http://mirror.centos.org/altarch/7/os/aarch64/Packages/gsl-1.15-13.el7.aarch64.rpm && yum -y localinstall gsl-1.15-13.el7.aarch64.rpm
- libpng: wget http://mirror.centos.org/centos/8-stream/AppStream/aarch64/os/Packages/libpng15-1.5.30-7.el8.aarch64.rpm && yum -y localinstall libpng15-1.5.30-7.el8.aarch64.rpm
- libfortran: wget http://mirror.centos.org/centos/8-stream/AppStream/aarch64/os/Packages/compat-libgfortran-48-4.8.5-36.1.el8.aarch64.rpm && yum -y localinstall compat-libgfortran-48-4.8.5-36.1.el8.aarch64.rpm
- jasper-libs: wget http://mirror.centos.org/altarch/7/os/aarch64/Packages/jasper-libs-1.900.1-33.el7.aarch64.rpm && yum -y localinstall jasper-libs-1.900.1-33.el7.aarch64.rpm
- jasper-devel: wget http://mirror.centos.org/altarch/7/os/aarch64/Packages/jasper-devel-1.900.1-33.el7.aarch64.rpm && yum -y localinstall jasper-devel-1.900.1-33.el7.aarch64.rpm

