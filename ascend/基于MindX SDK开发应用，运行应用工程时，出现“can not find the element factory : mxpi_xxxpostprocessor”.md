# 基于MindX SDK开发应用，运行应用工程时，出现“can not find the element factory : mxpi_xxxpostprocessor”

## 内核版本


## 问题现象
在使用MindX SDK开发并运行应用工程时，系统报错“can not find the element factory : mxpi_xxxpostprocessor”，尽管在$HOME/Ascend/mindx_sdk/<sdk_version_package>/opensource/bin路径下执行./gst-inspect-1.0 mxpi_xxxpostprocessor命令可正常加载该插件。

## 问题根因
gstreamer的历史缓存未清除，导致运行时无法正确识别已安装的插件。

## 解决方案
1. 确认环境已安装python3.9，并将libpython3.9.so.1.0拷贝至/usr/lib64/路径下；2. 根据运行环境架构执行命令 rm ~/.cache/gstreamer-1.0/registry.x86_64.bin（x86_64）或对应aarch64版本，清除gstreamer缓存后重新运行程序。

