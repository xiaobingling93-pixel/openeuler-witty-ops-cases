# 使用Volcano和Ascend Operator组件场景下，业务面故障的任务所有Pod的Status全部变为Failed，任务无法触发无条件重试重调度

## 内核版本


## 问题现象
在使用Volcano和Ascend Operator组件的场景中，当业务面发生故障时，任务的所有Pod状态均变为Failed，导致任务无法触发无条件重试或重调度机制。

## 问题根因
Volcano默认在任务所有Pod状态都变为Failed时，会将整个任务标记为失败状态，且不会自动触发无条件重试或重调度。

## 解决方案
用户需修改Volcano源码和任务YAML配置：1）在pkg/controllers/job/state/running.go中增加IgnoreAction处理逻辑；2）在vendor/volcano.sh/apis/pkg/apis/bus/v1alpha1/actions.go中定义IgnoreAction；3）在任务YAML的spec.policies中添加对PodFailed事件的Ignore动作，以允许任务在Pod全部失败后仍能触发重调度。

