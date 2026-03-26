# PyTorch模型训练时，AsStrided算子报错“the output element is out of input range”

## 内核版本


## 问题现象
将GitHub上的VoicePrintRecognition-PyTorch模型迁移至昇腾平台训练时，AsStrided算子编译失败，报错“Compile op[AsStrided] failed.Please check op’s compilation error message”，设备日志显示“OpName:[AsStrided] “the output element is out of range!””。

## 问题根因
AsStrided算子在编译时对输入输出shape校验失败，原因是模型中使用了生成负数的torch.complex64接口。

## 解决方案
设置环境变量 export COMBINED_ENABLE=1，用于优化非连续两个算子组合类场景。

