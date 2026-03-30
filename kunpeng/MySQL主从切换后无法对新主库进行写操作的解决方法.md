# MySQL主从切换后无法对新主库进行写操作的解决方法

## 内核版本


## 问题现象
MySQL主从切换后无法对新主库进行写操作，即新主库处于只读模式。

## 问题根因
MySQL主从切换前，从库设置了禁止写入（read_only=1），切换为主库后未将其修改为可写模式，导致新主库仍保持只读状态。

## 解决方案
执行以下SQL命令将新主库设置为可写模式：
1. 查看当前只读状态：show variables like 'read_only';
2. 关闭只读模式：set global read_only=0;
3. 再次确认只读状态已关闭：show variables like 'read_only';
之后即可对新主库正常执行写操作。参考图示：![](/doc_center/source/zh/kunpengdbs/ecosystemEnable/MySQL/zh-cn_image_0000001181303636.png)

