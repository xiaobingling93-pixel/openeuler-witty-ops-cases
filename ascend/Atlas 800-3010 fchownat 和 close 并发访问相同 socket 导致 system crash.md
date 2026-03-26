# Atlas 800-3010 fchownat 和 close 并发访问相同 socket 导致 system crash

## 内核版本


## 问题现象
在SLES15、Ubuntu16.04 LTS、Ubuntu 18.04 LTS、Oracle Linux 7系统上，并发执行fchownat和close系统调用操作同一个socket时，会触发'NULL pointer dereference'错误，导致系统崩溃。

## 问题根因
sockfs_setattr函数在执行过程中未增加文件描述符的引用计数，当同时执行close系统调用时，sock_release会将sock->sk置空，随后sockfs_setattr尝试访问sock->sk->sk_uid时发生空指针解引用。

## 解决方案
升级或安装对应的安全补丁：SLES15（kernel SUSE-SU-2019:0224-1）、Ubuntu 16.04 LTS（linux-hwe USN-3752-2）、Ubuntu 18.04 LTS（linux等 USN-3752-1）、Oracle Linux 7（Unbreakable Enterprise kernel ELSA-2018-4195）。

