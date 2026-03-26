# qwen2.5-32b推理报错内存不足

## 内核版本


## 问题现象
使用1.0.0-300I-Duo-py311-openeuler24.03-lts的Docker镜像在310P上部署qwen2.5-32b模型时，执行/usr/local/Ascend/atb-models/examples/run_pa.py报错NPU内存不足，提示NPU0卡内存不足（总容量43.24 GiB，已分配6.65 GiB，预留12.34 GiB）。

## 问题根因
Docker容器未挂载所有可用的NPU卡，导致模型仅使用部分NPU（如NPU0），而其他NPU（如npu6、npu7）处于空闲状态，资源未被合理分配和充分利用。

## 解决方案
在创建Docker容器时，将模型需要使用的全部NPU卡（如npu4、npu5、npu6、npu7）挂载进容器，并通过环境变量指定模型运行的NPU设备，例如：export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7。

