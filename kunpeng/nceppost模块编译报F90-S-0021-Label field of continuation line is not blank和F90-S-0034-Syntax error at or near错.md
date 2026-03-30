# nceppost模块编译报F90-S-0021-Label field of continuation line is not blank和F90-S-0034-Syntax error at or near错

## 内核版本


## 问题现象
NCEPLIBS构建安装中nceppost模块报F90-S-0021-Label field of continuation line is not blank和F90-S-0034-Syntax error at or near & (/path/to/NCEPLIBS/NCEPLIBE-1.2.0/download/emc_post/sorc/ncep_post.fd/CMASSI.f: 17)错。

## 问题根因


## 解决方案
1. 修改“/nceppost.dir/build.make”文件。
   1. 打开“/path/to/NCEPLIBS/NCEPLIBS-1.2.0/build/CMakeFiles/nceppost.dir/build.make”文件。
   2. 按“i”进入编辑模式，修改第123行的内容为：cd /path/to/NCEPLIBS/NCEPLIBS-1.2.0/build/nceppost/src/nceppost-build && sed -i "s/isystem/I/g" `grep -rl "isystem"` && $(MAKE)
   3. 修改后按“Esc”键，输入:wq!，按“Enter”保存并退出编辑。
2. 重新编译：make。

