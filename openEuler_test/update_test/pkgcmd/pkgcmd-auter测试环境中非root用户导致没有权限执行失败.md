# 标题
pkgcmd-auter测试环境中非root用户导致没有权限执行失败

# 基本信息
- 测试用例: oe_test_auter
- 系统版本: openEuler-24.03-LTS-SP3(aarch64/x86_64)
- 是否问题：否
- 关联issue：无

# 问题现象
执行用例oe_test_auter时候，auter --enable后grep enable报错，提示用例失败

# 错误日志

```
+ auter --enable
+ grep enabled
+ CHECK_RESULT 1 0 0 'Enable the failure'
+ actual_result=1
+ expect_result=0
+ mode=0
+ error_log='Enable the failure'
+ exit_mode=0
+ '[' -z '1 0 0 Enable the failure' ']'
+ '[' 0 -eq 0 ']'
+ test 1x '!=' 0x
+ test -n 'Enable the failure'
```

# 问题根因

auter --enable后grep不到enable信息，原因是auter命令需要root权限才能执行

# 解决方案
1. 更改为root权限后执行