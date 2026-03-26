# 编译和安装MySQL时执行make -j 96命令后报错的解决方法

## 内核版本


## 问题现象
在编译和安装MySQL过程中，执行 make -j 96 命令时，进度到55%时报错：c++: internal compiler error: Killed (program cc1plus)，并伴随多个 make 错误，最终导致编译失败。

## 问题根因
虚拟机运行内存不足，而C++模板的大量实例化扩展需要大量内存，导致编译器进程被系统终止。

## 解决方案
方法一：关闭虚拟机，增加其内存配置后重新启动。方法二：临时创建并启用交换空间（swap file），例如使用以下命令创建16GB交换文件：sudo dd if=/dev/zero of=/swapfile bs=64M count=256；sudo mkswap /swapfile；sudo swapon /swapfile；然后重新执行编译命令。编译完成后建议关闭并删除交换文件：sudo swapoff /swapfile；sudo rm /swapfile。若仍报错，可增大交换文件大小。

