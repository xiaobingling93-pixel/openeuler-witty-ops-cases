# petsc配置过程中报错

## 内核版本


## 问题现象
运行./configure后报错，提示脚本无法识别当前操作系统，建议下载最新的config.guess和config.sub脚本。

## 问题根因
config.guess和config.sub两个文件版本过旧，无法识别当前操作系统。

## 解决方案
1. 使用find ./ -name config.guess和find ./ -name config.sub命令查找这两个文件；2. 将文件内容分别替换为最新版本的内容，下载地址为：http://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.guess;hb=HEAD 和 http://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.sub;hb=HEAD。

