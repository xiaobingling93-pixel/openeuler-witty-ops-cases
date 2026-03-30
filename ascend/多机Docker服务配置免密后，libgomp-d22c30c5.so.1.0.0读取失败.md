# 多机Docker服务配置免密后，libgomp-d22c30c5.so.1.0.0读取失败

## 内核版本


## 问题现象
多机Docker服务配置免密后，运行时出现错误：libgomp-d22c30c5.so.1.0.0 cannot allocate memory in static TLS block，导致该动态库读取失败。

## 问题根因
执行pdsh命令时，导入的环境变量存在问题，特别是LD_PRELOAD未被正确设置或传递，导致程序无法正确加载libgomp-d22c30c5.so.1.0.0库。

## 解决方案
在每个节点上修改DeepSpeed的runner.py文件：1）将EXPORT_ENVS设为["NCCL", "PYTHON", "MV2", "UCX", "LD"]；2）显式设置LD_PRELOAD指向正确的libgomp-d22c30c5.so.1.0.0路径；3）在导出环境变量时确保包含LD_PRELOAD字段。

