# Kernels算子包安装报错

## 内核版本


## 问题现象
安装Kernels算子包时，系统提示依赖的软件包不存在，具体报错信息为：[ERROR] Kernel package depends on toolkit nnae or nnrt, none of these packages are installed in /usr/local/Ascend。

## 问题根因
Kernels包的安装依赖于CANN基础软件包（如Toolkit、NNAE或NNRT）中的至少一个，但当前系统未安装这些依赖包，也未正确配置相关环境变量。

## 解决方案
请先安装Toolkit、NNAE或NNRT中的任一CANN基础软件包，并配置好环境变量，再安装Kernels包。具体可参考《CANN 软件安装指南》。不同业务场景推荐的安装组合如下：训练&推理&开发调试场景安装Toolkit+Kernels；训练&推理场景安装NNAE+Kernels；边缘推理场景安装NNRT+Kernels。

