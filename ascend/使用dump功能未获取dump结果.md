# 使用dump功能未获取dump结果

## 内核版本


## 问题现象
日志显示正确执行了Dump功能，但在Dump结果路径下没有Dump的结果。日志信息包含“HandleDumpConfig end in HandleDumpConfig”和“set HandleDumpConfig success in aclInit”等关键字。

## 问题根因
Dump配置的模型名与实际的模型名不匹配。

## 解决方案
检查Dump配置文件acl.json，确保配置合法，特别是model_name是否配置正确。可通过ATC命令生成的模型json文件中查找"name"字段确认模型名称（位于"graph"字段外）和算子名称（位于"graph"字段内）。

