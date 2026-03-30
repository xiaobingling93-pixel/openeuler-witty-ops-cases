# 运行WarpAffineHiper或WarpPerspective接口出现Synchronize stream execution failed错误

## 内核版本


## 问题现象
运行WarpAffineHiper或WarpPerspective接口时，出现错误：Synchronize stream execution failed. (Calling Function = aclrtSynchronizeStream, Code = 507014, Message = "ACL error, please refer to the document of CANN.")

## 问题根因
输入shape过大或使用转换矩阵的计算量过大，导致aicore执行超时。

## 解决方案
使用数据切分方式拆分shape或改变转换矩阵以减少数据量。

