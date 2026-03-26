# 容器启动时提示Error running install command for nf_conntrack的解决方法

## 内核版本


## 问题现象
容器启动时提示“Error running install command for nf_conntrack”。

## 问题根因
容器启动需要开启nf_conntrack，但系统中存在禁用或冲突的nf_conntrack配置。

## 解决方案
1. 检查“/etc/modprobe.d/”和“/usr/lib/modprobe.d/”目录下.conf配置文件，注释掉其中nf_conntrack相关内容。
2. 按“Esc”键，输入:wq!，按“Enter”保存并退出编辑。
3. 重启服务器生效。

