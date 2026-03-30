# 启动OceanBase集群时提示not enough disk space的解决方法

## 内核版本


## 问题现象
启动OceanBase集群时提示：not enough disk space。

## 问题根因
部署OceanBase集群时，yaml配置文件中data_dir所在磁盘空间小于datafile_size配置值，或redo_dir所在磁盘空间小于log_disk_size配置值，导致系统判定磁盘空间不足。

## 解决方案
修改OceanBase部署所用的yaml配置文件（如example.yaml），将data_dir和redo_dir配置项指向空间足够大的磁盘路径（例如/sata/data和/sata/redo），保存并重新启动集群。

