# 模型转换时，Python版本不匹配，导致模型转换失败

## 内核版本


## 问题现象
输入模型转换命令后，系统报错E40002，提示当前Python版本为3.6.9，而系统仅支持Python 3.7或更高版本。

## 问题根因
ATC工具进行模型或单算子编译时依赖特定版本的Python（要求为Python 3.7.x、3.8.x或3.9.x），而当前环境中使用的Python版本为3.6.9，不在支持范围内。

## 解决方案
若未安装符合要求的Python版本，则需先安装；若已安装，则通过设置环境变量指定使用符合要求的Python版本（如Python 3.7.5）：export PATH=/usr/local/python3.7.5/bin:$PATH 和 export LD_LIBRARY_PATH=/usr/local/python3.7.5/lib:$LD_LIBRARY_PATH。

