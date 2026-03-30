# 安装MindCluster ToolBox后使用算力、带宽、功耗等功能报错：Failed to load the libascendcl.so dynamic library

## 内核版本


## 问题现象
Ascend DMI工具执行算力测试、带宽测试、功能测试等功能时报错，提示'Failed to load the libascendcl.so dynamic library. Check the environment configuration dependency.'

## 问题根因
未安装CANN软件包或未配置CANN软件的环境变量。

## 解决方案
参考《MindCluster Toolbox用户指南》中“环境配置”章节，安装对应软件包或配置环境变量。例如，若已安装ascend_toolkit开发插件包，可执行命令'source /usr/local/Ascend/ascend-toolkit/set_env.sh'导入环境变量，之后即可正常使用相关功能。

