# 安装MetaPhlAn时提示ssl异常

## 内核版本


## 问题现象
安装MetaPhlAn时提示ssl模块不可用，报错信息如图所示：![](/doc_center/source/zh/kunpenghpcs/hpcindapp/trouble/zh-cn_image_0000001208527372.png)

## 问题根因
ssl模块不可用。

## 解决方案
1. 执行以下命令重新编译Python，configure后面添加编译选项：
   ```
   ./configure --prefix=/path/to/Python-3.9.6  --enable-shared --enable-optimizations
   ```
2. 执行以下命令安装：
   ```
   make
   make install
   ```

