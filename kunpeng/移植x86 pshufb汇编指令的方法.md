# 移植x86 pshufb汇编指令的方法

## 内核版本


## 问题现象
编译报错：unknown mnemonic 'pshufb' -- 'pshufb'。

## 问题根因
pshufb是x86平台的汇编指令，在鲲鹏平台上不支持，需要替换为等效实现。

## 解决方案
将pshufb汇编指令替换为SSE intrinsic函数_mm_shuffle_epi8，并在鲲鹏平台上手动实现该函数：
FORCE_INLINE __m128i _mm_shuffle_epi8(__m128i a, __m128i b)
{
    uint8x16_t tbl = vreinterpretq_u8_m128i(a);
    uint8x16_t idx = vreinterpretq_u8_m128i(b);
    uint8_t __attribute__((aligned(16))) mask[16] = {0x8F, 0x8F, 0x8F, 0x8F, 0x8F, 0x8F, 0x8F, 0x8F,
0x8F, 0x8F, 0x8F, 0x8F, 0x8F, 0x8F, 0x8F, 0x8F};
    uint8x16_t idx_masked = vandq_u8(idx, vld1q_u8(mask));
    return vreinterpretq_m128i_u8(vqtbl1q_u8(tbl, idx_masked));
}

