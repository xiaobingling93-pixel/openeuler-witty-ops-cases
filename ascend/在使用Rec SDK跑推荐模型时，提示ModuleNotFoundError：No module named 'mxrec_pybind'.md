# 在使用Rec SDK跑推荐模型时，提示ModuleNotFoundError：No module named 'mxrec_pybind'

## 内核版本


## 问题现象
在使用Rec SDK跑推荐模型时，报错：ModuleNotFoundError：No module named 'mxrec_pybind'，找不到mxrec_pybind模块。

## 问题根因
在运行脚本中未正确配置Rec SDK安装路径。

## 解决方案
在运行脚本中参考如下配置，添加Rec SDK对应的安装路径、so文件路径，以及将so文件路径添加到环境变量LD_LIBRARY_PATH中：
rec_package_path="/usr/local/python3.7.5/lib/python3.7/site-packages/mx_rec"
so_path=${rec_package_path}/libasc
export LD_LIBRARY_PATH=${so_path}:/usr/local/lib:$LD_LIBRARY_PATH

