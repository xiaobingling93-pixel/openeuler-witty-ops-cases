# 编译libvirt 5.6.0概率性失败的解决方法

## 内核版本


## 问题现象
在按照《KVM虚拟机安装指南》中“（可选）升级libvirt”相关内容编译libvirt-5.6.0时，有62.5%的概率出现编译失败。错误信息包括：1) gcc报错找不到文件 '../src/libvirt_probes.o.dtrace-temp.c'；2) Python traceback显示OSError: [Errno 2] No such file or directory: '../src/libvirt_probes.o.dtrace-temp.c'。两种错误均与某个临时源码文件缺失有关。

## 问题根因
libvirt-5.6.0的Makefile存在缺陷，特别是在src/remote/Makefile.inc.am中，在并发编译场景下会导致dtrace生成的临时文件被提前删除或未正确生成，从而引发编译失败。

## 解决方案
修改/bin/dtrace文件，将第308行的keep_temps = False改为keep_temps = True，以保留临时文件，避免因文件缺失导致编译失败。修改后重新编译libvirt即可成功生成RPM包。

