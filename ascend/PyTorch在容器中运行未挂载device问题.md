# PyTorch在容器中运行未挂载device问题

## 内核版本


## 问题现象
在容器中运行PyTorch脚本时出现NPU相关ERROR，无法正常使用NPU设备。

## 问题根因
启动容器实例时未挂载必要的设备参数（如/dev/davinciX、/dev/davinci_manager等），导致容器内无法访问NPU设备。

## 解决方案
使用docker run命令重启容器，并正确挂载NPU相关设备和目录，例如：
docker run -it --ipc=host \
--device=/dev/davinciX \
--device=/dev/davinci_manager \
--device=/dev/devmm_svm \
--device=/dev/hisi_hdc \
-v /usr/local/Ascend/driver \
-v /usr/local/dcmi \
-v /usr/local/bin/npu-smi \
${镜像名称}:{tag} \
/bin/bash
其中X为NPU芯片物理ID号。

