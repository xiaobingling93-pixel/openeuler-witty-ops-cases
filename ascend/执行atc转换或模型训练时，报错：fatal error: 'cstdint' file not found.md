# 执行atc转换或模型训练时，报错：fatal error: 'cstdint' file not found

## 内核版本


## 问题现象
在Ubuntu 22.04上执行atc转换命令或者在CentOS 7.6上进行模型训练时，报错：fatal error: 'cstdint' file not found。

## 问题根因
可能原因一：Ubuntu 22.04环境上安装了多个gcc版本（如gcc 11和gcc 12），CCEC编译时使用了高版本gcc（如gcc 12），但该版本缺失cstdint头文件；可能原因二：CentOS 7.6系统默认gcc版本为4.8.5，即使已安装更高版本（如gcc 7.3.0），CCEC仍使用默认低版本的头文件，导致兼容性问题。

## 解决方案
若为原因一，卸载高版本gcc（如gcc-12）：apt remove gcc-12 libgcc-12-dev；若为原因二，在模型训练前配置环境变量C_INCLUDE_PATH和CPLUS_INCLUDE_PATH，指向Ascend工具链中对应gcc版本（如7.3.0）的头文件路径，例如：export C_INCLUDE_PATH=/usr/local/Ascend/ascend-toolkit/latest/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/:/usr/local/Ascend/ascend-toolkit/latest/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/aarch64-target-linux-gnu/，并相应设置CPLUS_INCLUDE_PATH。

