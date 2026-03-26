# 安装PyTorch后执行--test指令报“ERROR”

## 内核版本


## 问题现象
使用MindCluster Ascend Deployer工具安装PyTorch后，执行命令 'bash install.sh --test=pytorch' 报错“ERROR”，具体错误信息为“cannot allocate memory in static TLS block”。

## 问题根因
模型运行时依赖的三方库文件加载顺序受环境中glibc版本、三方库加载时机及依赖库版本等因素影响，在部分场景下无法顺利触发DTV表的扩容机制，导致DTV表耗尽，从而引发内存分配失败。

## 解决方案
通过设置LD_PRELOAD环境变量，优先加载报错中涉及的依赖库。具体操作为：编辑~/.bashrc文件，在末尾添加 'export LD_PRELOAD=$LD_PRELOAD:{报错信息中实际依赖库的路径}'，保存后执行 'source ~/.bashrc' 使配置生效。

