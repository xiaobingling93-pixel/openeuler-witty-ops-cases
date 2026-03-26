# 源码编译安装鲲鹏加速引擎时，找不到engine.h文件

## 内核版本


## 问题现象
在源码编译鲲鹏加速引擎的引擎层代码时，提示“engine.h: No such file or directory”错误。

## 问题根因
编译鲲鹏加速引擎的引擎层代码时需要依赖engine.h头文件，但编译器在默认路径中未找到该文件，且用户未配置包含该文件的搜索路径。

## 解决方案
1. 确保已根据《鲲鹏加速引擎 用户指南》中的“安装OpenSSL/Tongsuo”章节正确安装了OpenSSL。
2. 使用命令 find / -name engine.h 找到engine.h文件所在目录。
3. 将该目录添加到环境变量C_INCLUDE_PATH中：export C_INCLUDE_PATH=查询到的目录:$C_INCLUDE_PATH。
4. 使用 echo $C_INCLUDE_PATH 验证环境变量是否添加成功。

