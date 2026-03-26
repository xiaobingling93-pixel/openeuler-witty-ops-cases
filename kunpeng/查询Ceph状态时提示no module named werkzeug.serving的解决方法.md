# 查询Ceph状态时提示no module named werkzeug.serving的解决方法

## 内核版本


## 问题现象
查询Ceph状态时报告“no module named werkzeug.serving”。

## 问题根因
系统中未安装werkzeug模块。

## 解决方案
执行命令 pip install werkzeug 安装缺失的werkzeug模块。

