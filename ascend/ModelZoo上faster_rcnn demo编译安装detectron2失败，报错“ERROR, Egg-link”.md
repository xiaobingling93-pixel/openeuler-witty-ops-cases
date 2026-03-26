# ModelZoo上faster_rcnn demo编译安装detectron2失败，报错“ERROR, Egg-link”

## 内核版本


## 问题现象
在训练服务器上，从ModelZoo下载Faster_RCNN代码工程后，按照README执行编译安装detectron2时失败，报错AssertionError: Egg-link *** does not match installed location ***。

## 问题根因
1. build目录下存在旧版的.so文件未删除；2. 当前编译目录与上次编译位置不同，导致Egg-link路径不一致。

## 解决方案
1. 按照README执行命令 rm -rf build/**/\*.so 删除旧的编译产物；2. 删除detectron2.egg-info文件夹，清除旧的安装链接信息。

