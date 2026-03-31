# 标题
pkgmanage-升级失败

# 基本信息
- 测试用例: oe_test_pkg_manager02
- 系统版本: openEuler-24.03-LTS-SP3(aarch64)
- 是否问题：需进一步确认
- 关联issue：无

# 问题现象
pkgmanage的oe_test_pkg_manager02用例测试执行软件包升级过程中，用例提示升级失败。

# 错误日志

```
+ test -s /home/pkg_manager_folder/upgrade_fail_list
+ CHECK_RESULT 0 1 0 'Packages upgrade error !'
+ actual_result=0
+ expect_result=1
+ mode=0
+ error_log='Packages upgrade error !'
+ exit_mode=0
+ '[' -z 0 ']'
+ '[' 0 -eq 0 ']'
+ test 0x '!=' 1x
+ test -n 'Packages upgrade error !'
```

# 问题根因

升级过程中会执行脚本，执行脚本有fail|error|warn|fatal|problem|Invalid|Skip|no such|Cound not|conflicts|not found信息

出现这些问题的原因有下面几个

1. 有冲突导致升级失败无法进行安装
3. 软件包的升级安装脚本存在问题，譬如命令不存在等

# 解决方案
1）从 /home/pkg_manager_folder/upgrade_fail_list中确认是哪个软件包失败，然后在 /home/pkg_manager_folder/目录中找到对应的软件包查看日志

2）或者搭建虚拟机环境重新进行单包测试。