# 如何批量处理生成的npy文件名异常情况

## 内核版本


## 问题现象
生成的npy文件名与预期不符，造成转换dump数据文件异常。

## 问题根因
TensorFlow模型生成dump数据时，因tfdbg自身原因或运行环境原因，会出现tfdbg截断算子名，导致生成的npy文件名与预期不符。

## 解决方案
重新生成npy文件，使其文件名符合精度比对要求。具体步骤包括：1）执行TensorFlow工程并进入tfdbg调试模式；2）使用lt > tensor_name命令保存所有tensor名称；3）创建脚本pt_cmd.sh提取tensor_index并生成pt命令；4）在tfdbg中执行生成的命令以输出npy文件；5）将npy文件移至新目录；6）创建脚本index_to_tensorname.sh批量重命名npy文件，将算子名中的'/'替换为'_'，':'替换为'.'，确保文件名与TensorFlow算子名称一致。

