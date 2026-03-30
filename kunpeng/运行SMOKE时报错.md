# 运行SMOKE时报错

## 内核版本


## 问题现象
运行SMOKE时报错“Error: Cannot assign to a named constant at (1)......Error: Expecting END SUBROUTINE statement at (1)”.

## 问题根因
fitrxref.f:192代码空格位太长。

## 解决方案
1. 使用PuTTY工具，以root用户登录服务器。
2. 执行命令进入“Makefileinclude”文件所在路径：cd $SMK_HOME/subsys/smoke/src。
3. 执行以下命令修改“Makefileinclude”文件：
   a. 打开文件：vi Makefileinclude
   b. 按“i”进入编辑模式，修改内容为：EFLAG = -ffixed-line-length-132 -fno-backslash
   c. 按“Esc”键，输入:wq!，按“Enter”保存并退出编辑。

