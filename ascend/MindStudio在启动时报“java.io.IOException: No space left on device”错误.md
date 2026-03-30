# MindStudio在启动时报“java.io.IOException: No space left on device”错误

## 内核版本


## 问题现象
启动MindStudio失败，并报java.io.IOException: No space left on device错误信息。

## 问题根因
MindStudio长时间运行后，在/home/{username}/tmp目录下会产生较多临时文件。如果MindStudio异常关闭，这些临时文件可能无法自动删除，从而占据大量磁盘空间，导致再次启动时磁盘空间不足。

## 解决方案
手动清理/home/{username}/tmp目录下的临时文件，释放磁盘空间。

