# 安装依赖“Rgraphviz”失败

## 内核版本


## 问题现象
在安装MWASTools过程中，安装Rgraphviz_2.40.0依赖时提示ERROR：compilation failed for package ‘Rgraphviz’。

## 问题根因
Rgraphviz_2.40.0依赖中的config.guess文件过旧，未能识别aarch64架构。

## 解决方案
1. 解压Rgraphviz_2.40.0.tar.gz；2. 删除旧的config.guess文件（路径为./src/graphviz/config/config.guess和./src/graphviz/libltdl/config/config.guess）；3. 从http://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.guess;hb=HEAD下载最新的config.guess；4. 将新config.guess复制到上述两个目录；5. 重新打包并执行R CMD INSTALL Rgraphviz_2.40.0.tar.gz进行安装。

