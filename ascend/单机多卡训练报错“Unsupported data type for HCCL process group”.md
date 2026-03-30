# 单机多卡训练报错“Unsupported data type for HCCL process group”

## 内核版本


## 问题现象
在使用torch_npu 1.8.1.post1-20230220版本进行单机多卡训练时，出现错误提示“Unsupported data type for HCCL process group”。

## 问题根因
模型的buffers中包含uint8类型的tensor，而HCCL通信过程不支持该数据类型。

## 解决方案
在创建DistributedDataParallel对象之前，遍历模型的buffers，将dtype为torch.uint8的tensor转换为int类型，代码如下：
for n, m in model.named_buffers():
    if m.dtype == torch.uint8:
        m.data = m.data.int()

