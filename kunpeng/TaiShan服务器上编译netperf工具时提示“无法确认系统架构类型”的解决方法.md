# TaiShan服务器上编译netperf工具时提示“无法确认系统架构类型”的解决方法

## 内核版本


## 问题现象
下载netperf源码后，在鲲鹏服务器的Linux系统上执行configure命令时，出现“无法确认系统架构类型”的报错。

## 问题根因
netperf源码中的config.guess文件通过uname -m命令获取系统架构名称，在鲲鹏服务器上该命令返回aarch64，但config.guess文件中未包含aarch64架构，仅列出了ARM架构，导致无法识别。

## 解决方案
解决方案1：手动修改config.guess文件，将uname -m命令的输出映射为arm。解决方案2：修改config.sub文件，在case $basic_machine in区域的两处位置添加aarch64和aarch64-*支持，并在configure时显式指定--host=aarch64 --build=aarch64。

