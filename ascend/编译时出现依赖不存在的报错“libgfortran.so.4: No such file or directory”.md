# 编译时出现依赖不存在的报错“libgfortran.so.4: No such file or directory”

## 内核版本


## 问题现象
开发MindX SDK应用工程过程中，尝试编译工程时，出现“libgfortran.so.4: No such file or directory”报错信息。

## 问题根因
opensource文件中的so文件需要依赖libgfortran.so.4，但在编译环境中找不到该库文件。

## 解决方案
执行以下命令安装gfortran：
apt-get update
apt-get install gfortran-4（如果环境中找不到gfortran-4，也可以安装>=4的版本）。

