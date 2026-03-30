# 安装-torch--whl-提示-torch-1-5-0xxxx-与-torchvision-所依赖的版本不匹配

## 内核版本


## 问题现象
安装“torch-*.whl”时，提示“ERROR：torchvision 0.6.0 has requirement torch==1.5.0, but you'll have torch 1.5.0a0+1977093 which is incompatible”。

## 问题根因
安装torch时会自动触发torchvision进行依赖版本检查，环境中已安装的torchvision版本为0.6.0，其要求torch版本严格等于1.5.0，而实际安装的torch版本为1.5.0a0+1977093（预发布版本），与torchvision的依赖要求不一致，因此报错。

## 解决方案
该报错对实际使用无影响，torch已成功安装，无需额外处理。

