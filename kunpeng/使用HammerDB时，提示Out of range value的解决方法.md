# 使用HammerDB时，提示Out of range value的解决方法

## 内核版本


## 问题现象
使用HammerDB进行大规模数据测试（如1TB数据）时，系统提示“Out of range value”错误。

## 问题根因
当数据量特别大时，生成的数据值超出了MySQL中INT数据类型的表示范围，导致溢出错误。

## 解决方案
将HammerDB源码中定义的数据类型从INT修改为表示范围更大的BIGINT。具体操作是修改“/home/HammerDB-3.2/src/mysql”目录下的mysqlolap.tcl文件，将第53行和第133行中的INT类型改为BIGINT类型。

