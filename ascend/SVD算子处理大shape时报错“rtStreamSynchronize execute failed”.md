# SVD算子处理大shape时报错“rtStreamSynchronize execute failed”

## 内核版本


## 问题现象
SVD算子在处理大shape（如[3072, 3072]）时执行超时，报错“rtStreamSynchronize execute failed”，而将shape改为[768, 768]后可正常执行。

## 问题根因
该SVD算子未在自研AI CPU算子库（aicpu_kernel.json）中注册，仅在TensorFlow适配的TFKernel.so中实现。因此，执行时调用了TF Adapter路径，但该路径在处理大shape时性能不足导致超时（默认2.8秒超时）。

## 解决方案
采用规避方案，将SVD算子强制在CPU上执行，例如通过x=torch.randn((3072, 3072)).cpu()确保数据位于CPU，从而绕过昇腾设备上的超时问题。

