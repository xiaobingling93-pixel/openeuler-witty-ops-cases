# 执行编译安装Tengine命令时提示ngx_user.c的解决方法

## 内核版本


## 问题现象
执行编译安装Tengine命令时提示“src/os/unix/ngx_user.c”错误。

## 问题根因
可能是Tengine版本与系统不匹配导致的问题。

## 解决方案
1. 打开报错文件 ngx_user.c（路径：src/os/unix/ngx_user.c）；2. 将第36行代码 /*cd.current_salt[0] = ~salt[0];*/ 注释掉；3. 保存并退出编辑；4. 重新执行编译安装命令 make && make install。

