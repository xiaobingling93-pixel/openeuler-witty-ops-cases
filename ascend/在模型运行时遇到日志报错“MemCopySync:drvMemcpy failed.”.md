# 在模型运行时遇到日志报错“MemCopySync:drvMemcpy failed.”

## 内核版本


## 问题现象
模型运行过程中出现日志报错“MemCopySync:drvMemcpy failed.”，同时伴随shell报错信息如“NPU error code is:500002”、“aicpu timeout”以及“rtKernelLaunch:ErrCode=207001, desc=[module new memory error]”。具体表现为在执行torch.stack操作时失败，错误发生在对不同数据类型（fp32与fp16）的张量进行拼接时。

## 问题根因
问题的根本原因是stack算子的输入参数数据类型不一致。在减法运算中，由于操作数的数据类型不同（如xs为fp32，gt_bboxes为fp16），导致left、top结果为fp32，而right、bottom结果为fp16。当这些不同数据类型的张量传入torch.stack时，引发内存拷贝失败和内核执行错误。

## 解决方案
在调用torch.stack之前，将所有输入张量的数据类型统一（例如都转换为fp16或fp32），以确保数据类型一致，从而规避该问题。此外，可通过插入stream同步操作（如torch_npu.npu.current_stream().synchronize()）来精确定位错误发生的算子位置，辅助调试。

