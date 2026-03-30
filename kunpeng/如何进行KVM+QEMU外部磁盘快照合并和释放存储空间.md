# 如何进行KVM+QEMU外部磁盘快照合并和释放存储空间

## 内核版本


## 问题现象
在虚拟机运行状态下，尝试进行快照合并操作时失败，导致快照占用的存储空间不断增长且无法有效释放。

## 问题根因
使用了可能存在缺陷的操作系统和软件版本，或对KVM、QEMU及Libvirt的快照管理功能不熟悉，导致操作不当，进而影响快照合并的成功率。

## 解决方案
1. 使用推荐的操作系统和软件版本（openEuler 22.03 LTS SP3、QEMU 6.2.0-83、Libvirt 6.2.0-57）。
2. 在虚拟机运行状态下创建外部磁盘快照：
   virsh snapshot-create-as --domain VM_NAME SNAPSHOT_NAME SNAPSHOT_DESC --disk-only --diskspec vda,snapshot=external --atomic
3. 执行快照合并（blockcommit）：
   virsh blockcommit --domain VM_NAME vda --base path_to_base_snapshot --top path_to_top_snapshot --wait --verbose
4. 删除不再需要的快照文件（谨慎操作）：
   virsh snapshot-delete --domain VM_NAME SNAPSHOT_NAME --metadata
   rm path_to_snapshot
注意：不能删除初始虚拟机磁盘文件、最后一个外部磁盘快照，以及作为合并目标的基础快照。

