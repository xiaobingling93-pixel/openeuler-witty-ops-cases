# 使用命令安装Vision SDK时，出现libpython3.9.so.1.0报错

## 内核版本


## 问题现象
使用命令 ./Ascend-mindxsdk-mxvision_{version}_linux-{arch}.run --install 安装Vision SDK时，报错提示：libpython3.9.so.1.0: cannot open shared object file: No such file or directory。

## 问题根因
系统中缺少Python 3.9所需的共享库文件libpython3.9.so.1.0，该文件在当前编译或运行环境中未找到。

## 解决方案
将Python安装路径下的libpython3.9.so.1.0文件复制到系统库目录（如/usr/lib或/usr/lib64）中，以满足依赖要求。

