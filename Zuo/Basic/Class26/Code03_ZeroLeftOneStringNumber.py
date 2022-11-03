# -*- coding: utf-8 -*-

"""
@File: Code03_ZeroLeftOneStringNumber.py
@Author: Sarah Shen
@Time: 02/11/2022 17:37
"""


def get_num1(n: int):
    if n < 1:
        return 0
    return process(1, n)


def process(i: int, n: int):
    if i == (n - 1):
        return 2
    if i == n:
        return 1
    return process(i + 1, n) + process(i + 2, n)


def get_num2(n: int):
    if n < 1:
        return 0
    if n == 1:
        return 1
    cur = 1
    pre = 1
    tmp = 0
    for i in range(2, n + 1):
        tmp = cur
        cur += pre
        pre = tmp
    return cur


def get_num3(n: int):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return n
    base = [[1, 1], [1, 0]]
    res = matrix_power(base, n - 2)
    return 2 * res[0][0] + res[1][0]


def fi(n: int):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    base = [[1, 1], [1, 0]]
    res = matrix_power(base, n - 2)
    return res[0][0] + res[1][0]


def matrix_power(m: [[int]], p: int):
    res = [[0] * len(m[0]) for i in range(len(m))]
    for i in range(len(res)):
        res[i][i] = 1
        # res = 矩阵中的1
    t = m  # 矩阵的1次方
    while p != 0:
        if p & 1 != 0:
            res = product(res, t)
        t = product(t, t)
        p >>= 1
    return res


def product(a: [[int]], b: [[int]]):
    """ 两个矩阵乘完之后的结果返回 """
    n = len(a)
    m = len(b[0])
    k = len(a[0])
    ans = [[0] * m for i in range(m)]
    for i in range(n):
        for j in range(m):
            for c in range(k):
                ans[i][j] += a[i][c] * b[c][j]
    return ans


if __name__ == '__main__':
    for i in range(20):
        print(get_num1(i))
        print(get_num2(i))
        print(get_num3(i))
        print("============")
