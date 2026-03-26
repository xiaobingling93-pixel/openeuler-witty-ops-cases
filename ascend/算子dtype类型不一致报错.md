# 算子dtype类型不一致报错

## 内核版本


## 问题现象
在执行onnx2om进行模型导出时报错“op[xxx], The xxx op dtype is not same, type1:xxx, type2:xxx”，模型转换后推理失败，提示“Aicpu kernel execute failed”。具体表现为sub算子的两个输入数据类型不一致（如int32和int64），导致AICPU执行失败。

## 问题根因
TopK算子在当前版本中仅支持int32数据类型，但其下层算子（如Initializer、Gather或Div）的初始值默认为int64，导致在inftershape阶段后进行数据类型校验时失败。此外，动态shape模型在转换后生成PartitionedCall节点，掩盖了原始算子结构，增加了问题定位难度。

## 解决方案
1. 设置环境变量export DUMP_GE_GRAPH=2，生成GE图，在after_infershape.pbtxt文件中定位报错算子及其输入类型；2. 根据GE图回溯到原始ONNX模型，找到对应initializer节点（如名称为'1113'或'1114'），将其data_type修改为6（代表int32）；3. 使用onnx.save保存修改后的模型；4. 若存在多个不一致的initializer，可批量修改后再恢复不影响的部分；5. 修改完成后重新进行onnx2om转换和推理，直至成功。必要时可结合onnxsim工具简化模型辅助排查。

