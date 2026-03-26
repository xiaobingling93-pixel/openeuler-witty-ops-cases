# 关闭memory_optimization后发生core dump

## 内核版本


## 问题现象
在迁移TensorFlow模型时，关闭了memory_optimization功能（配置为RewriterConfig.OFF），导致程序发生core dump，错误信息为：tensorflow/core/grappler/optimizers/memory_optimizer.cc xxx (core dump)。

## 问题根因
无论memory_optimization开启或关闭，TensorFlow原生代码都应保证网络正常运行。关闭后出现core dump，说明是TensorFlow自身的问题。

## 解决方案
建议注释掉关闭memory_optimization的代码，即移除或注释以下配置以重新启用memory_optimization：# config.graph_options.rewrite_options.memory_optimization = RewriterConfig.OFF

