# 编译ROOT时报CMake Error at TBB-stamp错误

## 内核版本


## 问题现象
编译ROOT时出现CMake Error at TBB-stamp/TBB-download-RelWithDebInfo.cmake:49 (message): Command failed: 1，提示找不到文件。

## 问题根因
集群不能联网，导致CMake在构建过程中无法下载TBB依赖包。

## 解决方案
参考《CNVnator 0.4.1移植指南（CentOS 7.6）》中“配置编译环境 > 安装CMAKE”章节，将预先下载的TBB安装包放入CMAKE生成的对应文件夹内。

