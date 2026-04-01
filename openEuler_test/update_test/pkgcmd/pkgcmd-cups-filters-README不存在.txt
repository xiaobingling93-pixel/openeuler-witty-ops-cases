# 标题
pkgcmd “cups-filters README不存在”

# 基本信息
- 测试用例: oe_test_cups-filters_config
- 系统版本: openEuler-24.03-LTS-SP3(aarch64/x86_64)
- 是否问题: 否
- 关联issue: 无

# 问题现象
测试执行过程中，检查到软件包安装后的README文件不存在

# 错误日志
```
+ test -f /usr/share/doc/cups-filters/README
+ CHECK_RESULT 1 0 0 'cups-filters README does not exist'
+ actual_result=1
+ expect_result=0
+ mode=0
+ error_log='cups-filters README does not exist'
+ exit_mode=0
+ '[' -z '1 0 0 cups-filters README does not exist' ']'
+ '[' 0 -eq 0 ']'
+ test 1x '!=' 0x
+ test -n 'cups-filters README does not exist'
```

# 问题根因
1. cups-filters-help软件包未安装，README文件由cups-filters-help软件包提供，测试用例未在准备环节安装此包

# 解决方案
1. 在测试用例中的pre_test()方法中安装cups-filters-help软件包