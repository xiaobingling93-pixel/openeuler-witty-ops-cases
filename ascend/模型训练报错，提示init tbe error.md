# 模型训练报错，提示init tbe error

## 内核版本


## 问题现象
在使用Rec SDK进行模型训练时发生报错，提示“init tbe error”，且在plog日志中发现存在Import repository_manager_log error。

## 问题根因
可能缺失python第三方依赖库attrs，或者由其他算子错误导致tbe初始化失败。

## 解决方案
针对Python第三方依赖库attrs缺失问题，执行pip3 install attrs进行安装；同时需排查具体算子问题，待问题解决后重新启动模型训练。

