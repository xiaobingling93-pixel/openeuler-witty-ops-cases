# 持续刷屏waiting for finish，无法结束

## 内核版本
8.0.RC2

## 问题现象
在配置为7.0.0的nnrt环境中，使用6.0.RC2的MindCluster ToolBox和8.0.RC2的Toolkit及kernel执行ascend-dmi --dg -i aicore -s -q压测时，持续刷屏“waiting for finish”，且plog报错无法找到算子的config配置文件。

## 问题根因
环境中的7.0.0 nnrt与8.0.RC2 kernel版本不配套，导致无法找到算子包，程序卡在接口中一直等待完成。

## 解决方案
卸载Toolkit和nnrt后，重新按顺序安装Toolkit、kernel，最后安装与kernel配套版本的nnrt。

