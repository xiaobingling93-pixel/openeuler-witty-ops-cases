# SPECCpu 2006连跑提示libstdc++.so.6 cannot open shared object

## 内核版本
4.14.0-115.el7a.0.1.aarch64

## 问题现象
升级GCC到7.3.0后连续运行SPECCpu 2006时，报错提示“libstdc++.so.6: cannot open shared object file: No such file or directory”。

## 问题根因
虽然编译安装的GCC 7.3.0在/usr/local/gcc-7.3.0/lib64目录下已包含libstdc++.so.6库文件，但系统未将该路径加入动态链接库搜索路径中，导致SPECCpu运行时无法找到该共享库。

## 解决方案
在/etc/profile中添加环境变量LD_LIBRARY_PATH，指向GCC 7.3.0的lib64目录：执行 vi /etc/profile，添加 export LD_LIBRARY_PATH=/usr/local/gcc-7.3.0/lib64:$LD_LIBRARY_PATH，然后执行 source /etc/profile 使配置生效，最后重新执行测试。

