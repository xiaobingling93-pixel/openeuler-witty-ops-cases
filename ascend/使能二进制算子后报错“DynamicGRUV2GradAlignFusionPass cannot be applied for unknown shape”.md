# 使能二进制算子后报错“DynamicGRUV2GradAlignFusionPass cannot be applied for unknown shape”

## 内核版本


## 问题现象
将PyTorch框架RSAN模型迁移至NPU上训练时性能很差，使能二进制算子后报错：“op[DynamicGRUV2GradAlign], DynamicGRUV2GradAlignFusionPass cannot be applied for unknown shape.”

## 问题根因
走二进制算子的DynamicGRUV2GradAlign等算子不支持动态shape。

## 解决方案
将这些算子添加至黑名单，使其不走二进制算子路径。

