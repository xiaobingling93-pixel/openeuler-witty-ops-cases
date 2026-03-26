# SWAP分区过小导致系统异常的解决方法

## 内核版本


## 问题现象
在数据库测试过程中，执行Linux基础命令时提示“-bash: fork: Cannot allocate memory”，重启数据库后问题暂时消失，但后续测试中频繁出现数据库进程减少的情况。

## 问题根因
系统SWAP空间过小（仅4GB，以往为150GB），在内存紧张时SWAP被耗尽，触发OOM（Out Of Memory）机制，导致系统kill数据库进程，从而引发进程数减少和命令无法执行的问题。

## 解决方案
在不调整数据库内存配置的前提下，通过动态扩展SWAP分区解决：1. 使用dd命令创建200GB的空文件（dd if=/dev/zero of=/home/swap bs=1G count=200）；2. 使用mkswap命令将其格式化为SWAP空间；3. 使用swapon命令加载该SWAP空间；4. 为使配置永久生效，需在/etc/fstab中添加“/home/swap swap swap defaults 0 0”以实现开机自动挂载。

