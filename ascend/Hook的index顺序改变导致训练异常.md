# Hook的index顺序改变导致训练异常

## 内核版本


## 问题现象
训练过程中报错：AttributeError: 'xxxxHook' object has no attribute 'xxxx'，具体表现为在访问training_hooks[-1]时出现属性错误。

## 问题根因
迁移工具默认为Estimator脚本添加了NPUBroadcastHook，但在后续代码中对hooks列表的index顺序进行了修改，导致原本预期位于末尾的LogTrainRunHook被移位，访问training_hooks[-1]时实际获取的是其他Hook对象，从而引发属性错误。

## 解决方案
修改训练脚本中对hook列表的索引方式，将原访问training_hooks[-1]的地方改为training_hooks[-2]，以正确指向LogTrainRunHook对象。

