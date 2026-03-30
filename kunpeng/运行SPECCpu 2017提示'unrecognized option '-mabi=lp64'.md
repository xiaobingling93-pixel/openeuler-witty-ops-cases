# 运行SPECCpu 2017提示'unrecognized option '-mabi=lp64'

## 内核版本


## 问题现象
在CentOS 7.6上运行SPECCpu 2017的测试命令 ./runcpu -c ../config/Example-gcc-linux-aarch64.cfg intrate 时，提示“'unrecognized option '-mabi=lp64'”。

## 问题根因
系统自带的GCC 4.8.5版本不支持'-mabi=lp64'编译选项。

## 解决方案
升级GCC至7.3.0版本：1. 下载并解压gcc-7.3.0.tar.gz；2. 执行./contrib/download_prerequisites下载依赖；3. 配置编译选项并编译安装；4. 配置环境变量PATH；5. 更新libstdc++.so.6库并创建软链接；6. 在/etc/ld.so.conf中添加库路径并执行ldconfig；7. 为兼容ARM架构char类型差异，在gcc/g++/c++命令中全局增加-fsigned-char编译选项，通过包装脚本实现。

