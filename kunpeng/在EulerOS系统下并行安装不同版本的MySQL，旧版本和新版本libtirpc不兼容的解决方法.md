# 在EulerOS系统下并行安装不同版本的MySQL，旧版本和新版本libtirpc不兼容的解决方法

## 内核版本


## 问题现象
在EulerOS 2.0系统下并行安装不同版本的MySQL时，由于系统中已存在旧版本的libtirpc（Libtirpc-0.2.4-0.16.el7.aarch64），与新版本的libtirpc（Libtirpc-1.1.4-0.h5.eulerosv2r8.aarch64）存在依赖冲突，导致无法同时安装。报错信息包括：'cannot install both Libtirpc-0.2.4-0.16.el7.aarch64 and Libtirpc-1.1.4-0.h5.eulerosv2r8.aarch64' 和 'The operation would result in removing the following protected packages: systemd-udev'。

## 问题根因
操作系统中已安装的旧版本libtirpc与新版本libtirpc不兼容，两者存在文件或依赖冲突，导致包管理器无法同时保留两个版本。

## 解决方案
建议首先测试当前MySQL版本是否兼容旧版本的libtirpc，如果兼容则无需安装新版本；若必须使用新版本，则需确保不同版本的MySQL使用独立的安装目录、数据目录和端口以避免冲突。此外，应避免强制移除受保护的系统包（如systemd-udev）以免破坏系统稳定性。

