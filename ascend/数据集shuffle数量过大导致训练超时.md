# 数据集shuffle数量过大导致训练超时

## 内核版本


## 问题现象
训练过程中出现超时错误，日志显示shuffle buffer填充缓慢，在超时前仅填充了6232个样本（目标为10000），随后报错“Internal errors”、“model stream execute failed”并导致程序崩溃。

## 问题根因
当启用GetNext算子下沉时，NPU采用预处理与前后向计算并行的机制。若shuffle的buffer_size设置过大（如10000），预处理阶段无法在前向计算任务等待的时间内填满缓冲区，导致计算任务因长时间无数据输入而超时失败。

## 解决方案
可采取以下任一方法解决：1）根据实际能填充的数据量减少shuffle的buffer_size（例如从10000降至5000）；2）关闭GetNext算子下沉功能（设置enable_data_pre_proc=False），使预处理与计算串行执行，但可能带来性能损失。

