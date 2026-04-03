# 标题
pkgcmd-socat测试环境中无tty导致误报命令执行失败

# 基本信息
- 测试用例: oe_test_socat_filan
- 系统版本: openEuler-24.03-LTS-SP3(aarch64/x86_64)
- 是否问题：否
- 关联issue：无

# 问题现象
执行用例oe_test_socat_filan时候，filan -s之后grep tty未找到，提示用例失败

# 错误日志

```
+ filan -s
+ grep tty
+ CHECK_RESULT 1 0 0 'Check filan -s failed'
+ actual_result=1
+ expect_result=0
+ mode=0
+ error_log='Check filan -s failed'
+ exit_mode=0
+ '[' -z '1 0 0 Check filan -s failed' ']'
+ '[' 0 -eq 0 ']'
+ test 1x '!=' 0x
+ test -n 'Check filan -s failed'
```

# 问题根因

filan -s后grep不到tty导致失败原因1）非终端设备执行,误报；2）filan -s执行失败

# 解决方案
1. 找终端环境重新测试。
2. 确认执行环境是否在终端设备执行