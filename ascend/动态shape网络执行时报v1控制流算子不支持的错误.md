# 动态shape网络执行时报v1控制流算子不支持的错误

## 内核版本


## 问题现象
模型执行时出现错误：node node_name(node_type) is v1 control operator, which is not supported, please convert to v2 control operator。

## 问题根因
当前网络为动态shape网络，且存在TensorFlow V1版本的控制流算子，而动态shape网络的执行不支持V1版本的控制流算子，导致网络执行失败。

## 解决方案
将网络中的TensorFlow V1版本的控制流算子转换为V2版本。方式一（推荐）：在import tensorflow as tf后增加tf.enable_control_flow_v2()和tf.enable_resource_variables()；方式二：配置环境变量export ENABLE_FORCE_V2_CONTROL=1（注意可能存在转换失败的场景，如网络脚本中包含ref控制算子）。

