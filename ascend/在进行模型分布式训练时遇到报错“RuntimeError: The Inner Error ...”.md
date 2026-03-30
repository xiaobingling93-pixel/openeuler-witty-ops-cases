# 在进行模型分布式训练时遇到报错“RuntimeError: The Inner Error ...”

## 内核版本


## 问题现象
配置RANK_TABLE_FILE的场景下，在进行模型分布式训练时遇到报错“RuntimeError: The Inner Error ...”，并且打印的operator name是具体的通信算子。

## 问题根因
在ranktable建链方式中，不存在socket协商阶段，直接开始建链，建链阶段的超时时间由HCCL_CONNECT_TIMEOUT控制。相比原有协商建链方式，该方式可能因缺少协商阶段而更容易在建链阶段超时，导致原流程中能成功建链的情况在ranktable方式下却超时失败。

## 解决方案
修改环境变量HCCL_CONNECT_TIMEOUT，在原有超时时间基础上增加30秒（例如从120秒增加到150秒）：export HCCL_CONNECT_TIMEOUT=150，然后重新运行模型。

