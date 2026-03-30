# 构建TensorFlow pip软件包时有告警信息提示的解决办法

## 内核版本


## 问题现象
构建TensorFlow pip软件包时出现告警信息，提示'Package tensorflow.xla_aot_runtime_src.tensorflow.tsl.platform is absent from the packages configuration'，指出该包未包含在setuptools的packages配置中，可能导致分发不完整或配置模糊。

## 问题根因
setuptools版本兼容性问题。较新版本的setuptools对包发现机制进行了调整，要求使用find_namespace_packages()/find_namespace:替代旧的find_packages()/find:方法，而当前构建脚本未适配此变化。

## 解决方案
1. 查询当前setuptools版本：pip3 list | grep setuptools；2. 将setuptools降级至56.0.0版本：pip3 uninstall setuptools && pip3 install setuptools==56.0.0；3. 重新执行构建命令：./bazel-bin/tensorflow/tools/pip_package/build_pip_package ./output。

