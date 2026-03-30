# 安装CANN包时报错pip3：command not found

## 内核版本


## 问题现象
安装CANN软件包时，系统报错“pip3：command not found”，导致安装过程中断。

## 问题根因
CANN软件包的部分组件依赖pip3进行安装，但当前环境中pip3命令不可用，可能是由于未正确配置Python3及相关环境变量。

## 解决方案
以Python3.7.5为例，通过以下命令配置环境变量：
export LD_LIBRARY_PATH=/usr/local/python3.7.5/lib:$LD_LIBRARY_PATH
export PATH=/usr/local/python3.7.5/bin:$PATH
该设置仅对当前终端窗口有效；若需永久生效，可将上述命令写入~/.bashrc文件并执行source ~/.bashrc。注意：若系统中存在多个Python版本且需切换使用，不建议将路径写入~/.bashrc。

