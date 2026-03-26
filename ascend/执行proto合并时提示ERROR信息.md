# 执行proto合并时提示ERROR信息

## 内核版本


## 问题现象
用户在执行proto合并时遇到ERROR信息，主要表现为：1）自定义的message（如QuantParameter）与AMCT内置的amct_custom.proto中定义的message冲突；2）自定义LayerParameter中的字段编号（如208、1000000等）与AMCT或ATC（caffe.proto）中已有的编号重复；3）自定义的NormalizeParameter等message与ATC内置定义重复，虽无报错但会覆盖默认行为。

## 问题根因
Proto文件合并过程中，用户自定义的message名称或字段编号与昇腾工具链（AMCT或ATC）中已存在的定义发生冲突。Protocol Buffer要求同一message内的字段编号唯一，且不同proto文件在合并时若存在同名message或相同字段编号，会导致编译错误或隐式覆盖。

## 解决方案
用户应根据报错提示，修改custom.proto中自定义message的字段编号，确保其不与AMCT（amct_custom.proto）或ATC（caffe.proto）中已使用的编号重复；同时避免定义与内置message同名的结构。建议查阅相关工具链的proto定义文档，选择未被占用的编号范围（如大于1000000的私有编号）以规避冲突。

