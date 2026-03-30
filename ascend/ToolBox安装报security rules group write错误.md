# ToolBox安装报security rules group write错误

## 内核版本


## 问题现象
安装ToolBox时，报错提示：run failed on file /root does not meet with security rules group write. exiting

## 问题根因
当前安装目录/root不符合安全规则，存在组写入权限。

## 解决方案
执行命令 chmod 755 /root 修改/root目录权限，去除组写权限。

