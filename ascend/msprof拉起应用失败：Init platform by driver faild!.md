# msprof拉起应用失败：Init platform by driver faild!

## 内核版本


## 问题现象
使用msprof工具拉起应用时，执行报错：Init platform by driver faild!。

## 问题根因
未将昇腾驱动相关路径添加到环境变量LD_LIBRARY_PATH中，导致程序无法加载必要的驱动库。

## 解决方案
执行命令 export LD_LIBRARY_PATH=/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:$LD_LIBRARY_PATH，将驱动库路径加入LD_LIBRARY_PATH环境变量。

