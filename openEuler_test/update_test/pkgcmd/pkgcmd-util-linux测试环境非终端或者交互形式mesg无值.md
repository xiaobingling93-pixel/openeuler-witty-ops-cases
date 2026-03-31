# 标题
pkgcmd-util-linux测试环境非终端或者交互形式mesg无值

# 基本信息
- 测试用例: oe_test_mesg
- 系统版本: openEuler-24.03-LTS-SP3(aarch64/x86_64)
- 是否问题：否
- 关联issue：无

# 问题现象
执行用例oe_test_mesg时，会获取mesg的值，获取默认值是空，非预期的y和N。

# 错误日志

```
++ mesg
++ awk '{print $2}'
+ original_mesg_state=
+ LOG_INFO 'Original mesg state is .'
+ message='Original mesg state is .'
+ python3 /opt/os-autotest/libs/locallibs/mugen_log.py --level info --message 'Original mesg state is .'
Wed Mar 25 17:51:58 2026 - INFO  - Original mesg state is .
+ OLD_LANG=en_US.UTF-8
+ export LANG=en_US.UTF-8
+ LANG=en_US.UTF-8
+ LOG_INFO 'End to prepare the test environment.'
+ message='End to prepare the test environment.'
+ python3 /opt/os-autotest/libs/locallibs/mugen_log.py --level info --message 'End to prepare the test environment.'
Wed Mar 25 17:51:58 2026 - INFO  - End to prepare the test environment.
++ type -t run_test
+ '[' -n function ']'
+ run_test
+ LOG_INFO 'Start to run test.'
+ message='Start to run test.'
+ python3 /opt/os-autotest/libs/locallibs/mugen_log.py --level info --message 'Start to run test.'
Wed Mar 25 17:51:59 2026 - INFO  - Start to run test.
+ LOG_INFO 'Test mesg without arguments.'
+ message='Test mesg without arguments.'
+ python3 /opt/os-autotest/libs/locallibs/mugen_log.py --level info --message 'Test mesg without arguments.'
Wed Mar 25 17:51:59 2026 - INFO  - Test mesg without arguments.
+ local exp
+ local mesg_output
+ local verbose_output
+ [[ '' == \n ]]
+ exp=0
+ mesg
+ CHECK_RESULT 2 0 0 'mesg without arguments failed'
+ actual_result=2
+ expect_result=0
+ mode=0
+ error_log='mesg without arguments failed'
+ exit_mode=0
+ '[' -z '2 0 0 mesg without arguments failed' ']'
+ '[' 0 -eq 0 ']'
+ test 2x '!=' 0x
+ test -n 'mesg without arguments failed'
```

# 问题根因

1）非终端环境导致mesg获取值是空，从而导致用例失败

# 解决方案
1）使用终端环境重新测试。