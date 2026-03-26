# 基于KVM+QEMU创建的虚拟机部署在鲲鹏服务器上，不关闭虚拟机的情况下如何创建和删除虚拟机外部快照？

## 内核版本


## 问题现象
当前环境采用UOS操作系统 + debian源，基于KVM + QEMU创建的虚拟机部署在鲲鹏服务器上，使用snapshot-create-as命令创建了快照，但快照大小无限增长，快照链变长后无法缩短快照链。

## 问题根因
UOS操作系统下debian源的QEMU和libvirt版本较低，导致快照管理功能异常，无法有效合并和删除外部快照。

## 解决方案
建议将操作系统更换为openEuler 22.03 SP2，并使用Yum源自带的QEMU 6.2.0和libvirt 6.2.0版本。在此环境下，可通过以下步骤操作：1. 使用命令 'virsh snapshot-create-as --domain VM_NAME SNAPSHOT_NAME SNAPSHOT_DESC --disk-only --diskspec vda,snapshot=external --atomic' 创建外部快照；2. 删除快照前先执行 'virsh blockcommit --domain VM_NAME vda --base path_to_base_snapshot --top path_to_top_snapshot --wait --verbose' 合并快照；3. 然后执行 'virsh snapshot-delete --domain VM_NAME SNAPSHOT_NAME --metadata' 删除快照元数据，并手动删除快照文件。若不更换系统，则需升级当前debian源中的相关软件版本。

