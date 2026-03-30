# cgroup管理驱动不一致的解决方法

## 内核版本


## 问题现象
初始化Kubernetes集群时提示“detected 'cgroupfs' as the Docker cgroup driver. The recommended driver is 'systemd'.”，表明Docker使用的cgroup驱动与Kubelet期望的不一致。

## 问题根因
Docker的Cgroup Driver配置为'cgroupfs'，而Kubelet使用的是'systemd'，两者不一致导致警告或潜在兼容性问题。

## 解决方案
1. 使用命令 `docker info | grep Cgroup` 确认当前Docker的cgroup驱动。
2. 编辑 `/usr/lib/systemd/system/docker.service` 文件，在 `ExecStart=` 行添加参数 `--exec-opt native.cgroupdriver=systemd`。
3. 执行 `systemctl daemon-reload` 重新加载配置，然后运行 `systemctl restart docker` 重启Docker服务。
4. 再次执行 `docker info | grep Cgroup` 验证输出是否为 `Cgroup Driver: systemd`。

