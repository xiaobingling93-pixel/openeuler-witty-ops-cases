# 编译LZ4-java时提示“BUILD FAILED”

## 内核版本


## 问题现象
执行编译时提示错误信息：“failed to create task or type antlib:org-Apache.ivy.anctzeaolve”。

## 问题根因
没有找到ivy-2.5.0.jar。

## 解决方案
下载ivy-2.5.0.jar，执行命令：ant ivy-bootstrap。

