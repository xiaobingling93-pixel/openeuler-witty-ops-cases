# 运行make install进度100%后报错

## 内核版本


## 问题现象
运行make install进度100%后报错，报错信息为：“make[2]: *** No rule to make target '*/path/to/COPASI/*copasi-dependencies-master/bin/lib/libexpat.a', needed by 'copasi/CopasiSE/CopasiSE'. Stop.”

## 问题根因
libexpat.a在对应目录下不存在，因为在使用脚本安装依赖时该文件生成在同级的lib64目录下。

## 解决方案
1. 执行命令切换到copasi-dependencies-4.26.213目录：cd */path/to/COPASI*/copasi-dependencies-4.26.213；2. 执行命令将lib64目录下的文件复制到lib目录下：cp -r ./bin/lib64* ./bin/lib

