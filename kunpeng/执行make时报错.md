# 执行make时报错

## 内核版本


## 问题现象
执行make时报错，报错信息为：“error: invalid operands to binary != (have ‘va_list’ {aka ‘__va_list’} and ‘void *’)”。

## 问题根因
源码编程语言不规范。

## 解决方案
执行以下命令修改“htmshell.c”文件：1. 使用vim命令进入“htmshell.c”文件（vim lib/htmshell.c）；2. 定位到714行（:714）；3. 按“i”进入编辑模式，将第714行内容修改为“if (format != NULL)”；4. 按“Esc”键，输入:wq!保存并退出编辑。

