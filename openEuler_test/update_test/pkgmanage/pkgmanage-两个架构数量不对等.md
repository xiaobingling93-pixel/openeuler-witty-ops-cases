# 标题
pkgmanage-两个架构数量不对等

# 基本信息
- 测试用例: oe_test_pkg_manager01
- 系统版本: openEuler-24.03-LTS-SP3(aarch64)
- 是否问题：需要进一步确认
- 关联issue：无

# 问题现象
pkgmanage测试执行过程中，检查两个架构的软件包数量失败，提示两个架构的软件包数量不一致。

# 错误日志

```
grep -ci .rpm repo_packages_arm
+ arm_pkgs_num=286
++ grep -ci .rpm repo_packages_x86
+ x86_pkgs_num=269
+ [[ 286 -eq 269 ]]
+ echo 'The update two architectures are not equal in number'
+ grep 'The update two architectures are not equal in number' /home/pkg_manager_folder/check_pkg_num.log
The update two architectures are not equal in number
+ CHECK_RESULT 0 1 0 'The two architectures are not equal in number'
+ actual_result=0
+ expect_result=1
+ mode=0
+ error_log='The two architectures are not equal in number'
+ exit_mode=0
+ '[' -z 0 ']'
+ '[' 0 -eq 0 ']'
+ test 0x '!=' 1x
+ test -n 'The two architectures are not equal in number'
```

# 问题根因

1、个别软件包只构建单架构，所以会数目不一致

2、新增的软件包只一个架构构建成功，只出了一个架构的包

# 解决方案
1. 查看/home/pkg_manager_folder/update_dnf_list两个架构下的文件，比对是哪个二进制包多了，确认是否属于误报
2. 确认好差异的二进制包之后，除去白名单，剩余的需确认是否是工程构建问题或者是升级后只构建了单架构