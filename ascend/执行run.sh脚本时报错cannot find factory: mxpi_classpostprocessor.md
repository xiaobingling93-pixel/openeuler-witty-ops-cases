# 执行run.sh脚本时报错cannot find factory: mxpi_classpostprocessor

## 内核版本


## 问题现象
进入“MyFirstApp/src”目录执行./run.sh脚本时，报错提示无法找到模型后处理插件mxpi_classpostprocessor，具体错误包括“can not find the element factory: mxpi_classpostprocessor”和“create stream(classification) failed”。

## 问题根因
Python版本错误或环境变量未正确配置，导致系统无法找到所需的库文件。

## 解决方案
1. 检查Python版本是否为3.9.2，若不是则需安装；2. 将Python 3.9.2安装目录下的libpython3.9.so.1.0拷贝至/usr/lib64/路径下；3. 清除Gstreamer历史缓存（rm ~/.cache/gstreamer-1.0/registry.aarch64.bin）；4. 重新运行./run.sh脚本。

