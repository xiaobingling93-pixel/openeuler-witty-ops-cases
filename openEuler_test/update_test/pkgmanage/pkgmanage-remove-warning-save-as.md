# 标题
pkgmanage remove warning save as

# 基本信息
- 测试用例: oe_test_pkg_manager02
- 系统版本: openEuler-22.03-LTS-SP4(x86_64)
- 是否问题：否
- 关联issue：无

# 问题现象
pkgmanage测试用例执行remove过程中，卸载软件包有warning信息，用例会提示卸载失败。

# 错误日志

warning: /etc/tuned/profile_mode saved as /etc/tuned/profile_mode.rpmsave
warning: /etc/tuned/active_profile saved as /etc/tuned/active_profile.rpmsave

# 问题根因

出现该类问题的软件包在spec中的打包阶段打包配置文件的时候用了%config或者%config(noreplace)字段，这样就会触发到rpm软件包的保护机制，在安装或者卸载过程中涉及到配置文件就会被另存为带后缀的.rpmsave

# 解决方案
非问题，误报