# ATC模型转换时报错：[ASCEND_OPP_PATH] is invalid when loading the tiling lib

## 内核版本


## 问题现象
执行ATC模型转换时，报错提示“[ASCEND_OPP_PATH] is invalid when loading the tiling lib”。

## 问题根因
ASCEND_OPP_PATH环境变量的实际路径与set_env.sh脚本中配置的路径不一致，导致加载tiling库失败。

## 解决方案
1. 检查/usr/local/Ascend/ascend-toolkit/set_env.sh脚本中ASCEND_OPP_PATH指定的路径是否存在；2. 若路径不存在，将正确的路径写入该脚本，并执行source set_env.sh命令使配置生效。

