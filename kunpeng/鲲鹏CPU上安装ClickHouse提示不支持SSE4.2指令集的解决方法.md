# 鲲鹏CPU上安装ClickHouse提示不支持SSE4.2指令集的解决方法

## 内核版本


## 问题现象
在鲲鹏CPU的服务器上安装ClickHouse时，系统提示“SSE 4.2 not supported”。

## 问题根因
SSE是Intel的指令集，而鲲鹏CPU基于ARM架构，不支持Intel的SSE 4.2指令集。

## 解决方案
建议在鲲鹏平台通过源码编译安装ClickHouse。可使用鲲鹏DevKit提供的迁移工具，该工具能扫描出代码中使用的SSE指令，并给出相应的适配修改建议，以帮助将应用从x86平台迁移到鲲鹏平台。

