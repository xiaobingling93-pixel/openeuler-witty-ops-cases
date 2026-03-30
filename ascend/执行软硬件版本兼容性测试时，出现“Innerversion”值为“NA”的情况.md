# 执行软硬件版本兼容性测试时，出现“Innerversion”值为“NA”的情况

## 内核版本


## 问题现象
CANN包与驱动正常安装时，执行“软硬件版本兼容性测试”，回显信息中“Innerversion”字段显示为“NA”。

## 问题根因
异常结果对应的软件包实际安装路径下，配置文件缺失或文件异常。驱动需检查version.info，CANN需检查ascend_*xxx*_install.info（*xxx*为实际安装的CANN组件，如toolkit、nnrt、nnae、tfplugin）。

## 解决方案
卸载对应软件后重新安装，以恢复正常的配置文件。

