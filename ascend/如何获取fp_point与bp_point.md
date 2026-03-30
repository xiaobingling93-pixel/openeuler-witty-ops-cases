# 如何获取fp_point与bp_point

## 内核版本


## 问题现象
用户需要获取fp_point（前向传播打点算子）和bp_point（反向传播打点算子），用于采集训练迭代轨迹数据以进行性能分析。

## 问题根因
fp_point和bp_point分别指网络计算图中第一个实际参与计算的前向算子和第一个反向传播算子。由于训练过程中默认保存的是checkpoint和meta文件，缺乏完整的计算图结构信息，因此需要通过graph.pbtxt文件来定位这两个关键算子。

## 解决方案
1. 通过tf.io.write_graph或Estimator的model_dir参数生成graph.pbtxt文件；2. 在graph.pbtxt中从前向开始查找第一个非数据/存储类的计算算子（如MatMul）作为fp_point，其name字段即为fp_point值；3. 从文件末尾向前查找第一个包含gradients且非Assign/Const/NoOp等类型的计算算子作为bp_point；4. 建议将找到的算子名称与GE生成的图（ge_proto_xxxxx_Build.txt）进行比对，若存在命名差异（如后缀_1），应以GE图中的名称为准。

