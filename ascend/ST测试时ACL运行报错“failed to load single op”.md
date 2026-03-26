# ST测试时ACL运行报错“failed to load single op”

## 内核版本


## 问题现象
运行算子ST测试时，ACL阶段报错“failed to load single op”。

## 问题根因
该问题的根本原因是ATC编译阶段未成功生成OM模型，导致ACL无法加载模型。

## 解决方案
打开atc.log查看ATC编译日志，检查是否存在error信息，并根据具体报错定位算子编译失败的原因进行修复。

