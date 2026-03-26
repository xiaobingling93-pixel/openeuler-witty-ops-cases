# 安装MindCluster ToolBox成功，但使用时提示command not found

## 内核版本


## 问题现象
安装MindCluster ToolBox成功后，执行ascend-dmi命令时提示“command not found”。

## 问题根因
未导入MindCluster ToolBox的环境变量。

## 解决方案
执行命令 source /usr/local/Ascend/toolbox/set_env.sh 导入环境变量，之后即可正常使用ascend-dmi命令。

