# 快速定位npu-smi报错dcmi module initialize failed, ret is -8005

## 内核版本


## 问题现象
执行npu-smi命令时出现错误：dcmi module initialize failed, ret is -8005。

## 问题根因
可能原因包括：1）当前环境中的NPU卡未烧写efuse安全启动，但安装的驱动包启用了安全启动签名；2）Linux内核被升级，导致已安装的驱动与当前运行的内核版本不匹配；3）在Docker环境中，NPU卡被其他容器占用，且该卡型号（如D710）不支持共享模式。

## 解决方案
针对不同原因采取相应措施：1）确认设备是否启用安全启动，若未启用则需安装不带安全启动签名的驱动包；2）若内核升级导致驱动不匹配，可重装驱动使其适配当前内核，或手动安装对应内核头文件（如yum install kernel-devel 或 apt-get install -y linux-source），并考虑配置系统阻止自动更新内核；3）在Docker环境中，检查是否有其他容器占用了目标NPU卡（通过docker inspect查看ASCEND_VISIBLE_DEVICES），若卡不支持共享模式，则需确保同一时间仅一个容器使用该卡，或进行卡资源切分（谨慎操作）。

