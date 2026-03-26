# 校准过程中提示"IFMR node. Name:'layer_ifmr_op' Status Message: std::bad_alloc"信息

## 内核版本


## 问题现象
训练后量化校准过程中，对某层进行量化时提示内存错误："IFMR node. Name:'layer_ifmr_op' Status Message: std::bad_alloc"。

## 问题根因
量化时使用的数据量过大，超出了环境（CPU或GPU）可用内存容量，导致内存分配失败。

## 解决方案
1. 减少校准所用的数据量，例如降低batch_size或batch_num，可尝试使用batch_size * batch_num的最小值进行量化；2. 如果仅个别层的featuremap过大导致内存错误，可跳过该层，不对其进行量化。

