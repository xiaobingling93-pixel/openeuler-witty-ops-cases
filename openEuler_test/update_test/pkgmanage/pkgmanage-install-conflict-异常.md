# 标题
pkgmanage-install-conflict-异常

# 基本信息
- 测试用例: oe_test_pkg_manager01
- 系统版本: openEuler-24.03-LTS-SP3(aarch64)
- 是否问题：需要进一步确认
- 关联issue：无

# 问题现象
pkgmanage测试执行oe_test_pkg_manager01的install过程中，存在安装完everything的包之后从而安装epol的包两个包提供了一样的文件从而导致文件冲突，软件包安装不上。

# 错误日志

```
The downloaded packages were saved in cache until the next successful transaction.
You can remove cached packages by executing 'yum clean packages'.
Error: Transaction test error:
  file /usr/bin/typer from install of python3-typer-cli-0.13.1-1.oe2403sp3.noarch conflicts with file from package erlang-dialyzer-25.3.2.6-13.oe2403sp3.aarch64
```

# 问题根因

1、everything中的包安装完后安装epol软件包，两个软件包提供同样的文件，从而导致文件冲突，软件包安装不上。

# 解决方案
1. 因为属于不同的源，该问题是可以判定为非问题，但是需要找环境单独分别安装两个软件包，排查是否可以正常安装
2. 如果是同一个源的话，该问题判定为是问题，需要找开发进行修复