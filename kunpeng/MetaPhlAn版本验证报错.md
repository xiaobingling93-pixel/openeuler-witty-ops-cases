# MetaPhlAn版本验证报错

## 内核版本


## 问题现象
安装完成后，验证MetaPhlAn版本号时提示无法找到‘_bz2’模块。

## 问题根因
系统缺少bzip2依赖，导致Python在编译时未包含_bz2模块。

## 解决方案
1. 参照安装Python章节，先安装bzip2依赖；
2. 重新编译安装Python；
3. 然后参照安装MetaPhlAn章节重新安装MetaPhlAn。

