# calicoctl文件没有执行权限的解决方法

## 内核版本


## 问题现象
执行calicoctl命令时提示“-bash: /usr/bin/calicoctl: Permission denied”，无法查看节点信息。

## 问题根因
calicoctl文件缺少可执行权限。

## 解决方案
通过chmod命令赋予calicoctl文件可执行权限：chmod +x /usr/bin/calicoctl。

