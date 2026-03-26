# 命令行安装gcc依赖时提示找不到包、编译时GCC报错问题

## 内核版本


## 问题现象
在命令行安装gcc依赖时提示无法找到包，需要使用源码编译安装；在编译过程中gcc报错。

## 问题根因
部分下载源不提供对应的依赖包，且所需的lib库需要进行软连接配置。

## 解决方案
1. 下载gcc-7.3.0.tar.gz源码包；2. 清空/tmp目录以确保编译有足够临时空间；3. 安装bzip2等系统依赖（CentOS用yum，Ubuntu用apt-get）；4. 解压源码并进入目录，执行./contrib/download_prerequisites下载依赖，若失败则手动wget指定版本的gmp、mpfr、mpc和isl依赖包；5. 执行configure配置（指定--prefix避免与系统gcc冲突），然后make编译并make install安装；6. 根据需要配置LD_LIBRARY_PATH环境变量指向新安装的gcc lib64路径。

