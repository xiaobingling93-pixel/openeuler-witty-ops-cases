# 编译Faiss 1.7.4时提示CMake的版本过低

## 内核版本


## 问题现象
编译Faiss 1.7.4时，出现报错信息，提示“CMake 3.23.1 or higher is required.”。

## 问题根因
当前CMake的版本过低，Faiss 1.7.4需要配套CMake 3.23.1及以上版本。

## 解决方案
安装CMake 3.23.1或以上版本。对于x86环境，下载并运行cmake-3.23.1-linux-x86_64.sh安装脚本；对于aarch64环境，下载并运行cmake-3.23.1-linux-aarch64.sh安装脚本。安装时接受许可协议，并选择安装到/usr目录下，安装完成后可通过cmake --version验证版本。

