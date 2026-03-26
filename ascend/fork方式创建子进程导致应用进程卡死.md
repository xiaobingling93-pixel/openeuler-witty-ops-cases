# fork方式创建子进程导致应用进程卡死

## 内核版本


## 问题现象
多卡训练场景下，训练进程卡死、训练超时或DataLoader卡死。

## 问题根因
在Python 3.8~3.11版本中，使用fork方式创建子进程时，会复制主进程的锁状态，子进程中再次尝试获取锁时发生死锁，导致进程卡死。Python堆栈中包含fork关键字，C/C++堆栈中包含acquire_lock关键字，确认是fork引发的Python已知bug（参考：https://github.com/python/cpython/issues/74580）。

## 解决方案
有两种解决方式：1）升级Python至官方针对该问题发布的补丁版本（适用于Python 3.8~3.11）；2）修改业务代码，显式使用spawn或forkserver方式创建子进程，避免使用fork方式。若修改点较多，建议优先采用升级Python的方式。

