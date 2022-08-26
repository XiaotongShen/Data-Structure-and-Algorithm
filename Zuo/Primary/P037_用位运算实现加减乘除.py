# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/8.
Author: 
    Sarah Shen
Date: 
    2022/8/8
"""

# 位运算加减乘除写不明白，这里存疑，查漏补缺后再看
# 异或运算就是无进位相加
# 进位的结果是 & 之后向左移动一位
# 位运算实现加 ： 无进位相加(^) + 进位向左移动一位 (& <<)


def add(a, b):
    mask1 = 2 ^ 32
    max_int = 2 ^ 31
    min_int = 2 ^ 31 + 1

    a %= mask1
    b %= mask1
    while b != 0:
        res = (a ^ b) % mask1
        b = ((a & b) << 1) % mask1
        a = res
    return ~((res ^ max_int) ^ min_int) if (res & min_int) == res else res


def neg_num(n):
    return add(~n, 1)


def minus(a, b):
    if a >= b:
        return neg_num(add(b, neg_num(a)))
    else:
        return add(a, neg_num(b))


def minus(a, b):
    if a >= b:
        return add(a, add(~b, 1))
    else:
        return add(~add(b, add(~a, 1)), 1)

def multi(a, b):
    mask = 2 ^ 32
    a %= mask
    b %= mask
    ans = 0 % mask
    while b != 0:
        if (b & 1) != 0:
            ans = add(ans, a) % mask
        a <<= 1
        b >>= 1
    return ans


def is_neg(n):
    return n < 0


def div(a, b):
    m = neg_num(a) if is_neg(a) else a
    n = neg_num(b) if is_neg(b) else b
    res = 0
    for i in range(30, 0, -1):
        if (m >> i) >= n:
            m = minus(m, n << i)
    res = neg_num(res) if is_neg(a) ^ is_neg(b) else res
    return res


if __name__ == '__main__':
    x = 20
    y = 32

    print(add(x, y))
    print(minus(x, y))
    print(multi(x, y))
    print(div(x, y))

    # a =
    # b = 2147483648
    # print(a & b)
    # print(b)
