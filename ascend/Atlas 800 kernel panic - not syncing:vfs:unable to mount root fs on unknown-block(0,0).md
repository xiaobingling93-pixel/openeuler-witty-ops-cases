# Atlas 800 kernel panic - not syncing:vfs:unable to mount root fs on unknown-block(0,0)

## 内核版本


## 问题现象
系统启动失败，打印堆栈信息：kernel panic - not syncing: vfs: unable to mount root fs on unknown-block(0,0)。

## 问题根因
initramfs损坏导致系统无法挂载根文件系统。该损坏通常由驱动升级（如1822FC网卡驱动）过程中异常操作或系统环境异常引起，dracut在驱动更新时重新生成initramfs，若此过程异常则会导致initramfs损坏。

## 解决方案
挂载LiveCD或切换至其他操作系统（如CentOS 7.6），使用lsblk识别原系统磁盘及根分区，挂载根分区以修复损坏的根文件系统，然后重启系统。

