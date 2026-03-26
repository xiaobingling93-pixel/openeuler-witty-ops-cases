# 服务器开启lldp，查询邻居信息没有输出

## 内核版本


## 问题现象
多机拉起DeepSeek模型时，服务化拉起卡住。检查网络通信，服务器两边都开启了LLDP，在服务器上执行hccn_tool -i 0 -lldp -g命令，没有任何新邻居信息输出。

## 问题根因
交换机400GE端口未做拆分，导致物理链路未UP，物理指示灯不亮，LLDP无法正常工作。

## 解决方案
在交换机（CE9860）上执行命令将400GE端口拆分为2个200GE端口：port split dimension interface 400GE 1/1/1 split-type 2*200GE。拆分后端口物理指示灯亮起，再次执行hccn_tool -i 0 -lldp -g命令即可正常显示邻居信息。

