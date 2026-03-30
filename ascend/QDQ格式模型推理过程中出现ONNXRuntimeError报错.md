# QDQ格式模型推理过程中出现ONNXRuntimeError报错

## 内核版本


## 问题现象
QDQ（Quantize and DeQuantize）格式模型（如从TensorFlow转换或从PyTorch导出的量化感知训练QAT模型）在ONNX Runtime 1.8.0及以上CPU版本环境下推理时，出现ONNXRuntimeError报错。

## 问题根因
ONNX Runtime默认启用所有图优化，在执行优化过程中，模型与ONNX Runtime版本之间存在不兼容问题，导致报错。

## 解决方案
调用InferenceSession函数执行推理时，配置SessionOptions的图优化级别为ORT_DISABLE_ALL，禁用所有优化。示例代码：import onnxruntime as ort; import amct_onnx as amct; amct.AMCT_SO.graph_optimization_level = ort.GraphOptimizationLevel.ORT_DISABLE_ALL; ort_session = ort.InferenceSession('model.onnx', amct.AMCT_SO)

