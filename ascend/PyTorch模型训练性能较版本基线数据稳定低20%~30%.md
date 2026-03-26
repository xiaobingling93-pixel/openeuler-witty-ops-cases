# PyTorch模型训练性能较版本基线数据稳定低20%~30%

## 内核版本


## 问题现象
现场测试CenterNet模型的训练性能（iter_fps为110）仅为内部测试结果（iter_fps为140+）的约80%，性能稳定偏低20%~30%。

## 问题根因
机器出厂默认设置为省电模式，导致CPU频率较低，对于性能瓶颈在host预处理阶段的模型，限制了整体训练性能。

## 解决方案
执行命令 'cpupower frequency-set -g performance' 开启CPU高性能模式，并通过 'cpupower frequency-info' 验证设置是否生效。

