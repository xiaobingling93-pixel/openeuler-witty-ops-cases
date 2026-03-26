# K8s软件源网络访问被拒绝的解决方法

## 内核版本


## 问题现象
K8s源网络访问被拒绝。

## 问题根因
需要将K8s源替换成其他可用源。

## 解决方案
将K8s源替换为华为云源，执行命令：
cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://mirrors.huaweicloud.com/kubernetes/yum/repos/kubernetes-el7-aarch64
enabled=1
gpgcheck=1
repo_gpgcheck=0
gpgkey=https://mirrors.huaweicloud.com/kubernetes/yum/doc/yum-key.gpg https://mirrors.huaweicloud.com/kubernetes/yum/doc/rpm-package-key.gpg
EOF

