# 显示“xxx：command not found”的解决方法

## 内核版本


## 问题现象
在Jenkins流水线脚本中执行命令时提示“xxx：command not found”，但登录shell后能成功执行该命令。

## 问题根因
在服务器上修改的环境变量PATH未在Jenkins流水线脚本的执行环境中生效。

## 解决方案
方案一：在服务器的“~/.bashrc”文件中添加对应环境变量后，重启Jenkins服务（执行systemctl daemon-reload和systemctl restart jenkins）。方案二：创建“~/jenkins.bashrc”文件并添加对应命令的环境变量（如export HELLO_WORLD=/opt/path/helloworld和export PATH=$HELLO_WORLD/bin:$PATH），然后在流水线脚本中通过source ~/jenkins.bashrc加载。方案三：在Jenkins节点配置中添加环境变量，路径为“系统管理 > 节点管理 > 选择对应的节点 > 配置从节点 > 节点属性”。

