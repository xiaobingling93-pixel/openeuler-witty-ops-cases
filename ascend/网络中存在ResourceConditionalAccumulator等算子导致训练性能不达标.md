# 网络中存在ResourceConditionalAccumulator等算子导致训练性能不达标

## 内核版本


## 问题现象
OSMN等网络中存在大量的ResourceConditionalAccumulator、ResourceAccumulatorTakeGradient资源类算子，导致训练性能不达标。

## 问题根因
当前昇腾AI处理器默认采用计算全下沉模式，这些算子在昇腾AI处理器上执行时调度开销和内存拷贝开销大，导致训练性能不达标。

## 解决方案
需要通过使能混合计算能力，将此类算子留在Host侧执行。具体方法为：在TensorFlow配置中启用NpuOptimizer的mix_compile_mode选项，并关闭remapping和memory_optimization重写选项。

