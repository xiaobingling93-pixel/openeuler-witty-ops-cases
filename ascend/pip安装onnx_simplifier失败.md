# pip安装onnx_simplifier失败

## 内核版本


## 问题现象
在CentOS 7.6 Arm架构服务器、Python 3.7.5环境下，使用pip安装onnx_simplifier 0.3.10版本失败。

## 问题根因


## 解决方案
采用源码安装方式：1. 从GitHub获取onnx-simplifier v0.3.10源码及依赖requirements.txt；2. 下载并拷贝源码到目标位置；3. 使用pip3安装指定版本的依赖onnxoptimizer==0.2.7（通过豆瓣源）；4. 执行Python3 setup.py build和install进行构建与安装；5. 通过命令'simplifier -h'验证安装是否成功。

