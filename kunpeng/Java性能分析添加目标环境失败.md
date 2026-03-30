# Java性能分析添加目标环境失败

## 内核版本


## 问题现象
Java性能分析工具在添加目标环境时失败。

## 问题根因
可能原因包括：1）证书生效时间大于系统当前时间；2）SSH的安全配置不满足软件要求，例如MACs、HostKey、HostKeyAlgorithms或Ciphers等算法未正确配置或缺失。

## 解决方案
1. 若因系统时间问题，校准系统时间后重试。2. 若为SSH配置问题，请按以下步骤操作：
   a. 确保sshd_config中配置了支持的MACs算法（如hmac-sha2-256等），可通过ssh -Q mac查看支持情况。
   b. 确保/etc/ssh目录下存在ssh_host_ecdsa_key和ssh_host_ed25519_key，若无则使用ssh-keygen生成，并在sshd_config中配置HostKey路径。
   c. 检查HostKeyAlgorithms是否包含支持的算法（如ssh-ed25519等），必要时通过ssh -Q HostKeyAlgorithms确认并添加到sshd_config。
   d. 确保Ciphers配置包含支持的加密算法（如aes128-ctr等），可通过ssh -Q cipher查看支持列表。
   e. 在/etc/ssh/ssh_config中添加“GSSAPIAuthentication yes”。
   f. 修改完成后执行“systemctl restart sshd.service”重启SSH服务使配置生效。

