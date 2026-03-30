# 运行ST测试时报错“Failed to get device count”

## 内核版本


## 问题现象
运行ST测试用例时报错“Failed to get device count”。

## 问题根因
环境变量配置有误。

## 解决方案
参考以下配置环境变量：
# 修改为Ascend实际的安装路径，子目录需包含atc, acllib, opp
install_path="/usr/local/Ascend"

PATH=${install_path}/atc/bin:${install_path}/atc/ccec_compiler/bin:$PATH
export ASCEND_OPP_PATH=${install_path}/opp
export DDK_PATH=${install_path}
export NPU_HOST_LIB=${install_path}/acllib/lib64
export LD_LIBRARY_PATH=${install_path}/acllib/lib64
export PYTHONPATH=${install_path}/atc/python/site-packages:$PYTHONPATH
export PYTHONPATH=${install_path}/toolkit/python/site-packages:$PYTHONPATH
export PATH=${install_path}/toolkit/python/site-packages/bin:$PATH
export DDK_PATH=${install_path}

