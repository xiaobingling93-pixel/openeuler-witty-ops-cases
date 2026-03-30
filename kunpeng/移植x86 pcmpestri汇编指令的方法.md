# 移植x86 pcmpestri汇编指令的方法

## 内核版本


## 问题现象
编译报错Error: unknown mnemonic 'pcmpestri' -- 'pcmpestri'。

## 问题根因
pcmpestri是x86 SSE4指令集中的指令，在非x86架构（如鲲鹏ARM架构）上不被支持，因此编译时会报错。

## 解决方案
根据实际使用的模式（PCMPSTR_EQUAL_EACH | PCMPSTR_UBYTE_OPS | PCMPSTR_NEG_POLARITY），使用C代码重新实现该指令的功能。通过比较两个字符串对应位置的字节是否相等，返回首次匹配的位置索引。示例代码使用ARM NEON头文件并遍历字节进行比较，最终返回匹配结果。参考实现如下：

#include <arm_neon.h>
template <int MODE>
static inline int SSE4_cmpestri(int32x4_t str1, int len1, int32x4_t str2, int len2)
{
    __oword a, b;
    a.m128i = str1;
    b.m128i = str2;
    int len_s, len_l;
    if (len1 > len2)
    {
        len_s = len2;
        len_l = len1;
    }
    else
    {
        len_s = len1;
        len_l = len2;
    }

    //本例替换的模式STRCMP_MODE =
    // PCMPSTR_EQUAL_EACH | PCMPSTR_UBYTE_OPS | PCMPSTR_NEG_POLARITY
    int result;
    int i;
    for (i = 0; i < len_s; i++)
    {
        if (a.m128i_u8[i] == b.m128i_u8[i])
        {
            break;
        }
    }
    result = i;
    if (result == len_s)
    {
        result = len_l;
    }
    return result;
}

