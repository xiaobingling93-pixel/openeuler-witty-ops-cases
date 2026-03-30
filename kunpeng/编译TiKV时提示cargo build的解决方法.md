# 编译TiKV时提示cargo build的解决方法

## 内核版本


## 问题现象
编译TiKV时提示“error: failed to fetch https://github.com/rust-lang/crates.io-index”。

## 问题根因
这是由于使用了http和https代理。

## 解决方案
1. 在“$HOME/.cargo/config”文件中，添加以下内容：
[net]
git-fetch-with-cli = true
2. 重新编译TiKV。

