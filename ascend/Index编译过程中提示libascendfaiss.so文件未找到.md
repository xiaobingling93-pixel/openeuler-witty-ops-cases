# Index编译过程中提示libascendfaiss.so文件未找到

## 内核版本


## 问题现象
编译过程中，出现提示libascendfaiss.so not found。

## 问题根因
未能通过环境变量中的路径找到“libascendfaiss.so”文件。

## 解决方案
请确认“libascendfaiss.so”的路径（位于安装包lib下），并将其添加进“LD_LIBRARY_PATH”环境变量中。

