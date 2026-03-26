# 生成算子时提示报错：Failed to import Python module

## 内核版本


## 问题现象
生成算子时出现错误：Failed to import Python module [AttributeError: `np.float_` was removed in the NumPy 2.0 release. Use `np.float64` instead.]

## 问题根因
Python 3.9及以上版本默认安装NumPy 2.0，而当前CANN版本尚未适配NumPy 2.0，导致导入模块失败。

## 解决方案
将NumPy版本降级至1.26，执行命令：pip3 install numpy==1.26

