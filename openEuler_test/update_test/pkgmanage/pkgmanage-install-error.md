# 标题
pkgmanage-install-error

# 基本信息
- 测试用例: oe_test_pkg_manager01
- 系统版本: openEuler-24.03-LTS-SP3(aarch64)
- 是否问题：需要进一步确认
- 关联issue：无

# 问题现象
pkgmanage测试执行oe_test_pkg_manager01用例过程中，安装软件包有异常信息，用例提示安装失败。

# 错误日志

```
+ test -s /home/pkg_manager_folder/install_fail_list
+ CHECK_RESULT 0 1 0 'install package error !'
+ actual_result=0
+ expect_result=1
+ mode=0
+ error_log='install package error !'
```

# 问题根因

执行install过程中，安装日志中如果存在grep -inE "fail|error|warn|fatal|problem|Invalid|Skip|no such|Cound not|conflicts|not found类似字段后用例就会提示错误，然后保留软件包以及软件包卸载日志到/home/pkg_manager_folder/下

# 解决方案
1）从 /home/pkg_manager_folder/install_fail_list中确认是哪个软件包失败，然后在 /home/pkg_manager_folder/目录中找到对应的软件包查看日志确认是否异常

2）或者搭建虚拟机环境重新进行安装测试。