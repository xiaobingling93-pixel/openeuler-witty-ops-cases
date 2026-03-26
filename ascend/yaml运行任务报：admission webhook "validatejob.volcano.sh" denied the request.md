# yaml运行任务报：admission webhook "validatejob.volcano.sh" denied the request

## 内核版本


## 问题现象
使用 kubectl apply -f XXX.yaml 启动任务时，报错：admission webhook "validatejob.volcano.sh" denied the request: spec.task[0].template.spec.volumes[5].hostPath.path: Required value. template.spec.containers[0].volumeMounts[5].name: Not found: "ascend-add-ons".

## 问题根因
任务YAML文件中存在拼写错误，具体为挂载卷配置中将 hostPath 的字段名 "path" 错误地写成了 "ipath"，导致Volcano的准入控制器校验失败。

## 解决方案
检查并修正YAML文件中的拼写错误，将 "ipath" 改为正确的字段名 "path"，确保 volume 和 volumeMount 配置匹配且语法正确。

