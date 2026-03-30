# 使用msopst工具生成error report时，命令执行完未生成.csv文件

## 内核版本


## 问题现象
使用msopst工具生成error report时，命令执行完成后未生成预期的.csv文件。

## 问题根因
系统未安装pandas库，或已安装的pandas库在Python中无法正常导入（可能由于依赖缺失，如_bz2模块）。

## 解决方案
1. 安装pandas库（建议版本1.1.3及以上）：pip3 install pandas==1.1.3 --user；2. 若出现'_bz2'模块缺失错误，需参考相关文档修复该依赖问题。

