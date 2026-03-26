# HCCL集群通信失败

## 内核版本


## 问题现象
HCCL集群通信失败。

## 问题根因
可能的原因包括：多机节点的NPU device IP无法互相ping通；多机节点的NPU device的TLS配置不一致；或其他未明确说明的问题。

## 解决方案
1. 检查多机节点的NPU device IP是否能互相ping通：在每个节点上使用hccn_tool查询device IP，并从另一节点执行ping测试，若不通则检查网络配置；IPv6地址需使用对应参数。2. 检查各节点NPU device的TLS配置是否一致，通过hccn_tool -tls -g命令查看并确保配置相同，如有差异需按文档调整。3. 其他问题可参考《集合通信接口参考》的FAQ章节。

