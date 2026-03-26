# 在Jenkins流水线内启动服务失败的解决方法

## 内核版本


## 问题现象
在Jenkins流水线中，当兼容性测试的启动命令涉及shell脚本时，若在conf配置文件中使用“nohup sh shell.sh”的形式，会导致目标应用服务启动失败。

## 问题根因
执行“nohup sh shell.sh”命令时，目标应用并未真正以nohup（后台启动）的形式运行，导致Jenkins流水线无法正确维持服务进程。

## 解决方案
将nohup命令移至shell.sh脚本内部，在调用时仅使用“sh shell.sh”，避免在脚本外部使用nohup。

