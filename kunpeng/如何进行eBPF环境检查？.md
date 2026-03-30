# 如何进行eBPF环境检查？

## 内核版本
4.1及以上

## 问题现象
系统无法支持eBPF功能，可能表现为内核参数未正确配置、缺少必要的内核头文件或build目录无指向文件，导致在宿主机或Docker容器中无法运行eBPF任务。

## 问题根因
eBPF功能依赖特定的内核配置（如CONFIG_BPF=y、CONFIG_BPF_SYSCALL=y等）和完整的内核头文件环境。若内核版本低于4.1，或相关配置未启用，或/lib/modules/$(uname -r)/build目录未正确链接到内核源码，则eBPF环境不满足运行条件。

## 解决方案
1. 使用zcat /proc/config.gz或cat /boot/config-$(uname -r)检查内核参数是否包含CONFIG_BPF=y、CONFIG_BPF_SYSCALL=y、CONFIG_BPF_JIT=y，以及根据内核版本确认CONFIG_HAVE_BPF_JIT=y（4.1–4.6）或CONFIG_HAVE_EBPF_JIT=y（4.7+）；2. 检查/lib/modules/$(uname -r)/build是否存在并正确指向内核源码目录；3. 若缺失，CentOS系统执行yum install kernel-headers kernel-headers.aarch64，Ubuntu系统执行sudo apt-get install linux-headers-$(uname -r)；4. 若仍无指向，可手动链接至/usr/src/kernels/$(uname -r)；5. 如问题持续，建议使用openEuler 20.03（LTS）操作系统。

