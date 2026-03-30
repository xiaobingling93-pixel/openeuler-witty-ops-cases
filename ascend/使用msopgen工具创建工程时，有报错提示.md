# 使用msopgen工具创建工程时，有报错提示

## 内核版本


## 问题现象
使用msopgen工具创建工程时，报错显示“xlrd.biffh.XLRDError: Excel xlsx file; not supported”。

## 问题根因
xlrd更新到了2.0.1版本，只支持.xls文件，而pandas.read_excel('xxx.xlsx')尝试读取.xlsx文件导致报错。官方资料要求xlrd版本为1.2.0。

## 解决方案
执行如下命令安装指定版本的xlrd依赖：pip3 uninstall xlrd --user && pip3 install xlrd==1.2.0 --user

