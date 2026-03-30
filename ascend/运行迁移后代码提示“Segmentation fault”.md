# 运行迁移后代码提示“Segmentation fault”

## 内核版本


## 问题现象
运行转换后的代码时没有报错，仅提示“Segmentation fault”信息。

## 问题根因
可能原因一：代码中引用了tensorboard或包含tensorboard的第三方库（如wandb、transformers），这些库在昇腾环境下存在兼容性问题。可能原因二：训练脚本中存在两个0维Tensor在不同设备（如CPU和NPU）上进行比较的操作，该操作在torch_npu上不被支持。

## 解决方案
针对原因一：注释掉相关的Summary、Writer调用，这些功能主要用于日志记录和绘图，不影响模型训练和精度收敛。针对原因二：修改代码，确保参与比较的两个0维Tensor位于同一设备上，例如将CPU上的Tensor显式迁移到NPU后再进行比较。

