# 标题
pkgmanage-remove-error

# 基本信息
- 测试用例: oe_test_pkg_manager01
- 系统版本: openEuler-24.03-LTS-SP3(aarch64)
- 是否问题：需进一步确认
- 关联issue：无

# 问题现象
pkgmanage的oe_test_pkg_manager01用例测试执行remove 软件包过程中，用例提示卸载失败。

# 错误日志

```
test -s /home/pkg_manager_folder/remove_fail_list
CHECK_RESULT 0 1 0 'Remove packages error !'
actual_result=0
expect_result=1
mode=0
error_log='Remove packages error !'
```

# 问题根因

执行remove过程中，卸载日志中如果存在fail|error|warn|fatal|problem|Invalid|Skip|no such|Cound not|conflicts|not found类似字段后用例就会提示错误，然后保留软件包以及软件包卸载日志到/home/pkg_manager_folder/下

# 解决方案
1）从 /home/pkg_manager_folder/remove_fail_list中确认是哪个软件包失败，然后在 /home/pkg_manager_folder/目录中找到对应的软件包查看日志

2）或者搭建虚拟机环境重新进行测试。