# 编译TiKV时提示找不到libisl.so.15的解决方法

## 内核版本


## 问题现象
在编译TiKV的时候，出现了找不到“libisl.so.15”动态库的问题，提示“error while loading shared libraries: libisl.so.15: cannot open shared object file: No such file or directory”。

## 问题根因
动态库缺失或动态库路径设置不正确。

## 解决方案
1. 使用 find / -name libisl.so.15 或 whereis libisl.so.15 查找库文件位置；2. 检查 /etc/ld.so.conf 文件确认库路径是否包含该库所在目录；3. 执行 ldconfig 命令使库文件生效；4. 重新编译TiKV。

