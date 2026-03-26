# 多颗NPU芯片故障后，导致Volcano重启，重调度任务不触发

## 内核版本


## 问题现象
多颗NPU芯片同时故障，导致Volcano调度模块崩溃并重启，进而引发故障重调度任务不执行；或出现状态为UnexpectedAdmissionError的Pod记录（但该情况不影响任务最终以新Pod正常运行）。

## 问题根因
NPU芯片故障后，Kubernetes将故障芯片移除。当Volcano尝试归还Pod占用的NPU资源时，发现本地记录的NPU芯片数量与Kubernetes集群中当前可用的NPU芯片数量不一致，从而触发panic导致Volcano崩溃重启。

## 解决方案
该问题是Volcano v1.4.0版本（开源社区版）的已知问题，可通过手动删除Volcano调度器Pod使其重建来恢复。执行命令：kubectl delete pod -n volcano-system volcano-scheduler-xxxxxxxxx（需替换为实际Pod名称）。

