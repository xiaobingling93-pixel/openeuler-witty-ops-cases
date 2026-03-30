# 运行make NWChem_config时报错

## 内核版本


## 问题现象
运行make NWChem_config时报错，报错信息为：“guess-mpidefs: command not found...”。

## 问题根因
未将GlobalArray软件包解压到“src/tools”目录，且该机器不能访问互联网。

## 解决方案
将GlobalArray软件包解压到“src/tools”目录或机器联网。

