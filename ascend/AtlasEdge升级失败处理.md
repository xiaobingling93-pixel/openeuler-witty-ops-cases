# AtlasEdge升级失败处理

## 内核版本


## 问题现象
用户在对AtlasEdge进行升级操作时，提示AtlasEdge升级失败。适用于MindX Edge 3.0.0及以下版本。

## 问题根因
用户未按照标准升级和回退操作执行，在升级hpm大包时出现AtlasEdge升级失败的场景。

## 解决方案
1. 通过命令行卸载当前版本软件，例如在安装目录“/opt/middleware/AtlasEdge/”执行 ./run.sh uninstall；2. 或通过SmartKit进行批量卸载，参考《MindX Edge 应用部署指南》中“如何批量卸载预置的软件版本，重新安装新版本”章节；3. 卸载完成后，重新按照升级流程和约束执行hpm大包的升级。

