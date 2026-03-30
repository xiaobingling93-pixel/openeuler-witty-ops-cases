# MindCluster ToolBox环境变量脚本配置失败

## 内核版本


## 问题现象
执行MindCluster ToolBox的环境变量配置脚本set_env.sh时，出现报错信息：'/root/mxIndex does not comply with security rules group write. exiting' 或 '[root@******] does not comply with security rules other write. exiting'。

## 问题根因
执行命令的用户和部分文件的权限或属组不同，导致目录权限不符合安全规则（如目录具有组写权限或其他用户写权限）。

## 解决方案
方法一：执行 unset LD_LIBRARY_PATH 后重新 source 脚本；方法二：检查并修改报错路径及其上层目录的权限为755；方法三：临时手动设置 PATH 和 LD_LIBRARY_PATH 环境变量以规避问题。

