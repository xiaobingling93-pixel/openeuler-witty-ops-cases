# 标题
pkgmanage remove Protected

# 基本信息
- 测试用例: oe_test_pkg_manager01
- 系统版本: openEuler-24.03-LTS(aarch64)
- 是否问题：否
- 关联issue：无

# 问题现象
pkgmanage测试执行过程中，卸载软件包有Error：受保护的软件包信息，提示卸载失败。

# 错误日志

Error: 
 Problem: The operation would result in removing the following protected packages

# 问题根因

1、软件包卸载时候会一起卸载掉安装依赖的软件包，会存在安装依赖的软件包是系统anaconda系列受到保护的软件包，那部分是不允许卸载的

如何确认需要卸载的包列表方法

    while read -r pkg; do
        grep "^${pkg}$" anaconda_list || echo "${pkg}" >>removeList
    done <update_list
# 解决方案
非问题误报