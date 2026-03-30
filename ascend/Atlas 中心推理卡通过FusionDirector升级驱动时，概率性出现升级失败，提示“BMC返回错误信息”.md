# Atlas 中心推理卡通过FusionDirector升级驱动时，概率性出现升级失败，提示“BMC返回错误信息”

## 内核版本


## 问题现象
通过FusionDirector升级驱动时，概率性出现升级失败，提示“BMC返回错误信息”，日志显示davinci节点被占用，具体报错为“The davinci nodes are occupied by some processes, please stop processes and install or uninstall again.”

## 问题根因
FusionDirector升级NPU驱动过程中，iBMA查询了NPU信息，导致davinci节点被iBMA占用，从而引发驱动升级失败。

## 解决方案
通过FusionDirector重新升级目标版本的驱动和固件。

