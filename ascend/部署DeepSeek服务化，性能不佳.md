# 部署DeepSeek服务化，性能不佳

## 内核版本
低于5.10

## 问题现象
部署DeepSeekV3/R1服务后实测性能较差，与预期存在较大差异。

## 问题根因
可能的原因包括：1）日志级别设置过高（如debug/info），导致大量日志打印影响性能；2）操作系统内核版本低于5.10；3）未通过环境变量CPU_AFFINITY_CONF进行CPU绑核优化，导致跨NUMA访问和调度开销增加；4）启用了确定性计算（HCCL_DETERMINISTIC=true），限制了性能优化。

## 解决方案
1）在set_env.sh中将各组件日志级别调整为ERROR；2）升级操作系统内核至5.10或更高版本（需研发确认）；3）设置CPU_AFFINITY_CONF环境变量进行绑核优化，推荐使用细粒度绑核（export CPU_AFFINITY_CONF=2）；4）关闭确定性计算（export HCCL_DETERMINISTIC=false）。

