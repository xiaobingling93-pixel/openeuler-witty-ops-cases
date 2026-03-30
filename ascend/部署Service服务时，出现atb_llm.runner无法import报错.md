# 部署Service服务时，出现atb_llm.runner无法import报错

## 内核版本


## 问题现象
部署Service服务时，Python无法导入atb_llm.runner模块，报ImportError错误。

## 问题根因
系统中使用的Python版本不是配套的3.10版本，或者pip命令对应的Python版本不是目标3.10版本，导致无法找到或加载atb_llm.runner包。

## 解决方案
1. 编辑~/.bashrc文件，添加对应Python 3.10安装路径的环境变量（如LD_LIBRARY_PATH和PATH）；2. 执行source ~/.bashrc使环境变量生效；3. 创建python和pip命令到Python 3.10对应可执行文件的软链接（例如：ln -s /usr/local/python3.10.13/bin/python3.10 /usr/bin/python 和 ln -s /usr/local/python3.10.13/bin/pip3.10 /usr/bin/pip）。

