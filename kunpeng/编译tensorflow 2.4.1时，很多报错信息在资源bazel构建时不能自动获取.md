# 编译tensorflow 2.4.1时，很多报错信息在资源bazel构建时不能自动获取

## 内核版本


## 问题现象
构建TensorFlow 2.4.1过程中，由于网络问题，Bazel无法自动下载所需依赖资源，导致报错。错误通常表现为无法获取特定URL指向的压缩包（如c83ed7ea9eb5fb3b93d1ad52b59750f1958b8bde.tar.gz）。

## 问题根因
网络问题导致Bazel在构建过程中无法访问外部资源URL以自动下载依赖项。

## 解决方案
1. 使用grep命令在构建目录和Bazel缓存目录（/root/.cache/bazel/_bazel_root）中搜索缺失资源的文件名，定位到引用该资源的.bzl文件及行号；
2. 编辑该文件，注释掉原始url，并将url修改为本地文件路径（如file:///path/to/tenflor_requires/c83ed7ea9eb5fb3b93d1ad52b59750f1958b8bde.tar.gz）；
3. 手动创建本地目录并使用wget命令下载对应依赖包；
4. 重复上述步骤处理后续构建中出现的其他类似依赖缺失问题，直至所有依赖解决并进入编译阶段。

