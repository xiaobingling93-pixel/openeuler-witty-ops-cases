# 退出HPC并行应用调试失败的解决方法

## 内核版本


## 问题现象
退出HPC并行应用调试失败，表现为环境清理失败、调试环境清理等待时间过长、退出MPI调试失败。

## 问题根因
可能原因包括rank启动数目过多或网络连通性不佳。

## 解决方案
1. （可选）手动清理提示路径下的文件：rm -f xxx；2. 释放进程资源：通过ps -ef | grep mpirun查找mpirun进程，并使用kill -15 {pid}终止对应进程；3. 重启服务：systemctl restart gunicorn_framework.service 和 systemctl restart gunicorn_plugin.service。

