# Atlas 800-3010 Ubuntu 16.04.5 KWE内核下dmesg报大量ACPI Exception

## 内核版本
4.15.0-29

## 问题现象
在2288H V5服务器上安装Ubuntu 16.04.5后，dmesg日志中打印大量ACPI Exception信息。

## 问题根因
该问题属于Linux内核bug，由于内核处理机制变化导致，参考Ubuntu官网链接：https://bugzilla.kernel.org/show_bug.cgi?id=198167。

## 解决方案
升级BIOS至A800-3010 1.0.8或更高版本，通过BIOS屏蔽该问题。

