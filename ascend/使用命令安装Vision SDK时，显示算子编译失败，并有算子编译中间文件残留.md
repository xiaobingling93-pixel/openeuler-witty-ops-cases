# 使用命令安装Vision SDK时，显示算子编译失败，并有算子编译中间文件残留

## 内核版本


## 问题现象
使用命令 ./Ascend-mindxsdk-mxvision_{version}_linux-{arch}.run --install 安装 Vision SDK 时，报错提示 CMake 版本过低（例如：CMake xxx or higher is required. You are running version xxxx），导致算子编译失败，并在安装路径下的 operators/operatorsdsl/op 目录中残留多个中间文件，如 gen_impl_and_mrege_json.sh、install.sh 等。

## 问题根因
系统中安装的 CMake 版本低于 Vision SDK 所需的最低版本，导致编译过程中断，进而产生中间文件残留。

## 解决方案
1. 使用 ./Ascend-mindxsdk-mxvision_{version}_linux-{arch}.run --uninstall 命令卸载已安装的软件包，并手动清除残留的中间文件；2. 根据 Vision SDK 对应操作系统的要求，升级 CMake 至兼容版本；3. 重新执行安装命令完成安装。

