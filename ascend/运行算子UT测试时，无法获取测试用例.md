# 运行算子UT测试时，无法获取测试用例

## 内核版本


## 问题现象
运行UT测试用例时，MindStudio配置界面无法显示测试用例。

## 问题根因
MindStudio通过执行Python命令在out目录下生成用例名的json文件来获取Case Name，无法获取测试用例的主要原因包括：1. Python环境缺少对应依赖；2. 用例指定了芯片类型，但SoC Version选择了不支持的芯片类型；3. 使用了add_case接口进行UT测试，该接口仅做编译，不支持Simulator_TMModel。

## 解决方案
1. 尝试切换SoC Version和Target，排查是否由芯片类型不匹配或使用add_case接口导致问题；2. 若仍无Case Name显示，需查看日志文件定位具体错误：Windows端通过“Help > Show Log in Explorer”打开idea.log，Linux端日志位于~/.cache/Huawei/MindStudioMS-5.0/log/idea.log，可从中提取执行命令并单独运行以查看失败原因。

