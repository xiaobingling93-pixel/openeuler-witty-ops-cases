# 如何查询鲲鹏916模组的PID、BID和CID？

## 内核版本


## 问题现象
用户需要查询鲲鹏916模组的PID（产品标识）、BID（主板标识）和CID（组件标识），但不清楚具体方法。

## 问题根因
CID信息查询依赖iBMC，而当前模组发布的iBMC功能单一，不支持查询CID信息；BID和PID可通过OS命令或日志收集功能获取。

## 解决方案
BID和PID可通过以下方法查询：方法一，在OS命令行执行ipmitool fru命令；方法二，通过一键收集日志功能查询，路径为“dump_info\RTOSDump\versioninfo\fruinfo”，再使用ipmitool fru命令查看。CID信息目前无法通过iBMC查询。

