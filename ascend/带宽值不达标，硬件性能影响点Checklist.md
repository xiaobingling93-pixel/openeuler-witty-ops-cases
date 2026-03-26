# 带宽值不达标，硬件性能影响点Checklist

## 内核版本


## 问题现象
在进行带宽测试时，实测带宽值未达到预期标准。

## 问题根因
可能由以下硬件配置问题导致：1. 服务器BIOS电源策略未设置为高性能模式；2. 内存条规模或安装方式不满足带宽交织要求；3. SMMU（系统内存管理单元）功能开启，增加了CPU处理页表的开销，影响Host到Device（h2d）的数据传输性能。

## 解决方案
1. 在服务器BIOS中将电源策略（Power Policy）设置为Performance模式（X86路径：Advanced > Socket Configuration > Advanced Power Mgmt. Configuration；ARM路径：Advanced > Performance Config）。2. 通过BMC界面检查内存条总数与在位情况，确保满足带宽交织要求。3. 在BIOS的Advanced > MISC Config中将Support Smmu设置为Disable，并保存重启。

