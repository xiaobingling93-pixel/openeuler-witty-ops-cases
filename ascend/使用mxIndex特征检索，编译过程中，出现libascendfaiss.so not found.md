# 使用mxIndex特征检索，编译过程中，出现libascendfaiss.so not found

## 内核版本


## 问题现象
在使用mxIndex进行特征检索的编译过程中，系统报错提示“libascendfaiss.so not found”，导致编译失败。

## 问题根因
系统未正确配置libascendfaiss.so动态库的路径，该库位于Ascend安装包的lib目录下，但未被包含在LD_LIBRARY_PATH环境变量中，导致链接器无法找到该共享库。

## 解决方案
将libascendfaiss.so所在的路径（通常为Ascend安装目录下的lib子目录）添加到LD_LIBRARY_PATH环境变量中，例如执行：export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/path/to/ascend/lib，然后重新编译。

