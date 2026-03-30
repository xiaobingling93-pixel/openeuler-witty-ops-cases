# 编译CMAQ时报错

## 内核版本


## 问题现象
编译CMAQ时报错，报错信息为：Error:Syntax in COMMON statement at (1) STATE3.EXT:174:27。

## 问题根因
数据格式错误，具体为STATE3.EXT文件中末尾若干行的行尾存在多余的“&”符号。

## 解决方案
执行以下命令修改“STATE3.EXT”文件：1. 打开文件：vim ioapi/STATE3.EXT；2. 进入编辑模式，删除末尾若干行行尾的“&”符号（参考图片：/doc_center/source/zh/kunpenghpcs/hpcindapp/trouble/zh-cn_image_0000001218070945.jpg）；3. 保存并退出：按Esc键，输入:wq!后回车。

