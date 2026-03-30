# SIESTA编译安装，执行7步骤时出现报错

## 内核版本


## 问题现象
编译安装SIESTA，执行步骤7时报错，报错信息为：configure: error: cannot guess build type; you must specify one
make: *** [FoX/.config] Error 1

## 问题根因
SIESTA源码中自带的config.guess脚本版本过旧（最后修改于2006-12-08），无法识别当前操作系统类型，导致configure脚本无法猜测构建系统类型。

## 解决方案
从http://savannah.gnu.org/cgi-bin/viewcvs/*checkout*/config/config/config.guess 和 http://savannah.gnu.org/cgi-bin/viewcvs/*checkout*/config/config/config.sub 下载最新的config.guess和config.sub文件，替换路径“/path/to/SIESTA/siesta-4.0.2/SRC/Fox/config”下的对应文件，然后执行make clean命令并重新编译。

