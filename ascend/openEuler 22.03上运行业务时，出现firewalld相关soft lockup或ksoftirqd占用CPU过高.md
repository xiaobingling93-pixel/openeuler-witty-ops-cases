# openEuler 22.03上运行业务时，出现firewalld相关soft lockup或ksoftirqd占用CPU过高

## 内核版本
openEuler 22.03

## 问题现象
在openEuler 22.03上同时使用默认的18.09版本docker与1.0.2版本firewalld时，运行业务出现firewalld相关soft lockup或ksoftirqd占用CPU过高的情况。

## 问题根因
18.09版本docker基于iptables写入规则，1.0.2版本firewalld基于nftables写入规则，两者无法匹配，导致系统软锁定或软中断处理进程ksoftirqd占用CPU过高。

## 解决方案
编辑“/etc/firewalld/firewalld.conf”文件，将FirewallBackend字段修改为iptables。

