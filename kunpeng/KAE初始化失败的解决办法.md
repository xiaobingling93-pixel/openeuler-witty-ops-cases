# KAE初始化失败的解决办法

## 内核版本


## 问题现象
使用KAE加速OpenSSL时报错或者没有加速效果。

## 问题根因
可能原因包括：加速器驱动未加载成功、KAE软连接未正确建立、OpenSSL引擎库路径的环境变量未配置。

## 解决方案
1. 检查加速器驱动是否加载成功，确认uacce.ko、qm.ko、sgl.ko、hisi_sec2.ko、hisi_hpre.ko、hisi_rde.ko、hisi_zip.ko模块已加载；2. 检查KAE和wd库是否在对应目录（如/usr/local/lib/engines-1.1或/usr/local/lib/engines-3.0）正确安装并建立了软连接；3. 确保通过export命令设置了OPENSSL_ENGINES环境变量，例如：export OPENSSL_ENGINES=/usr/local/lib/engines-1.1（OpenSSL 1.1.1x）或export OPENSSL_ENGINES=/usr/local/lib/engines-3.0（OpenSSL 3.0.x）。

