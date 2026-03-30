# 运行和验证CMAQ执行测试时报错

## 内核版本


## 问题现象
运行和验证CMAQ执行测试时，提示缺少“libnetcdf.so”库。

## 问题根因
环境变量中未加载相应变量。

## 解决方案
请在进行测试时加入环境变量：
setenv LD_LIBRARY_PATH /path/to/CMAQ/NETCDF/lib:$LD_LIBRARY_PATH

