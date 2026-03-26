# msKPP工具运行kernel时提示权限错误

## 内核版本


## 问题现象
运行kernel时出现报错：PermissionError: Path /any_path/_gen_module.so cannot have write permission of group.

## 问题根因
当前用户创建的文件的默认权限过大，具有group写权限。

## 解决方案
使用umask -S命令查询当前权限配置，然后执行umask 0022命令调整权限配置，使文件权限变为u=rwx,g=rx,o=rx。

