# ST测试时ACL单算子匹配模型失败，报错提示“[Match][OpModel]MatchOpModel”

## 内核版本


## 问题现象
ST测试时ACL单算子匹配模型失败，报错提示“[Match][OpModel]MatchOpModel”。

## 问题根因
模型加载时及模型执行时的算子信息不匹配，包括静态或动态单算子模型的shape、attr、isConst等字段不一致。

## 解决方案
运行ST测试时通过配置环境变量“export ASCEND_GLOBAL_LOG_LEVEL=0”打开debug日志，在~/ascend/log下查看模型加载时的关键日志“Register model. OpModelDef =”及模型执行时的关键日志“OpExecutor::ExecuteAsync aclOp =”，确认加载和执行时模型中的算子信息是否匹配。静态模型要求所有字段完全一致；动态模型除shape和shapeRange外其余字段需一致，且执行时的shape必须在模型定义的shapeRange范围内。

