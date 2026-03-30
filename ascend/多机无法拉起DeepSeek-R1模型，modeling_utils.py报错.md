# 多机无法拉起DeepSeek-R1模型，modeling_utils.py报错

## 内核版本


## 问题现象
在服务化拉起过程中，出现错误：if metadata.get("format") not in ["pt", "tf", "flax", "mix"]: AttributeError: "NoneType" object has no attribute 'get'。

## 问题根因
输入的权重中缺少metadata字段。

## 解决方案
1. 排查日志modeling_utils.py报错；2. 安装更新transformers版本为4.46.3。

