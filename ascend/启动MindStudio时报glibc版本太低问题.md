# 启动MindStudio时报glibc版本太低问题

## 内核版本


## 问题现象
在CentOS 7.6系统中启动MindStudio时，报错“Error: failed /home/MindStudio/jbr/lib/server/libjvm.so...”，导致无法正常启动。

## 问题根因
系统中的glibc版本低于2.27，而MindStudio自带的jbr（Java Runtime）依赖更高版本的glibc，因此无法正常运行。

## 解决方案
1. 删除MindStudio安装目录下的jbr文件夹；2. 检查系统是否已安装Java 11（通过which java和java -version命令）；若未安装，则执行sudo yum install -y java-11-openjdk；3. 若系统存在多个Java版本，使用sudo alternatives --config java命令切换至Java 11版本。注意：此操作可能导致与JBR相关的部分功能受限。

