# 编译Spark时提示Cannot find 'R_HOME'的解决方法

## 内核版本


## 问题现象
编译Spark时提示错误：Cannot find 'R_HOME'. Please specify 'R_HOME' or make sure R is properly installed。

## 问题根因
编译Spark时启用了R语言支持，但系统未安装R语言或未正确设置R_HOME环境变量。

## 解决方案
1. 成功编译安装R语言（例如安装在“/opt/tools/installed”目录），并设置好R_HOME环境变量；2. 再次执行编译Spark命令，如：dev/make-distribution.sh --tgz -Pyarn,hive,hive-thriftserver,spark。

