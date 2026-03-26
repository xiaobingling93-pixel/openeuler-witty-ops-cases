# Tensor比对报错：The data in dump file have zero

## 内核版本


## 问题现象
执行Vector比对时，界面弹出报错窗口，提示dump数据文件包含0。

## 问题根因
“Output”栏显示的dump数据文件中包含0，导致无法计算。

## 解决方案
删除“Output”栏显示的dump数据文件后，再执行Vector精度比对。

