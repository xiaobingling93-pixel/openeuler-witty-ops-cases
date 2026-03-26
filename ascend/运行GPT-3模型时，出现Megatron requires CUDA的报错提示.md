# 运行GPT-3模型时，出现Megatron requires CUDA的报错提示

## 内核版本


## 问题现象
在NPU环境下运行基于PyTorch的GPT-3模型时，系统报错提示“Megatron requires CUDA”。

## 问题根因
该问题的根本原因是在NPU（而非GPU）环境中缺少对Megatron框架的适配。具体包括：1）未安装专用于NPU的megatron_npu包；2）虽然已安装megatron_npu，但Python环境未能正确找到该包的路径，导致程序回退到默认依赖CUDA的Megatron实现。

## 解决方案
若未安装megatron_npu，需从指定仓库克隆源码并以可编辑模式安装：执行 'git clone https://gitee.com/ascend/Megatron-LM.git megatron_npu'，然后进入目录执行 'pip install -e .'。若已安装但路径未被识别，需将megatron_npu的绝对路径添加到PYTHONPATH环境变量中，可在shell中执行 'export PYTHONPATH=megatron_npu包绝对路径:$PYTHONPATH'，或在Dockerfile中通过 'ENV PYTHONPATH=megatron_npu包绝对路径:$PYTHONPATH' 设置。

