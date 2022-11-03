# -*- coding: utf-8 -*-

"""
@File: Code02_FibonacciProblem.py
@Author: Sarah Shen
@Time: 02/11/2022 17:37
"""


def f1(n: int):
    """ 暴力递归的方法 """
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    return f1(n - 1) + f1(n - 2)


def f2(n: int):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    res = 1
    pre = 1
    tmp = 0
    for i in range(3, n + 1):
        temp = res
        res = res + pre
        pre = temp
    return res


# O(logN)
def f3(n: int):
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


def s1(n: int):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return n
    return s1(n - 1) + s1(n - 2)


def s2(n: int):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return n
    res = 2
    pre = 1
    tmp = 0
    for i in range(3, n + 1):
        tmp = res
        res = res + pre
        pre = tmp
    return res


def s3(n: int):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return n
    base = [[1, 1], [1, 0]]
    res = matrix_power(base, n - 2)
    return 2 * res[0][0] + res[1][0]


def c1(n: int):
    if n < 1:
        return 0
    if n == 1 or n == 2 or n == 3:
        return n
    return c1(n - 1) + c1(n - 3)


def c2(n: int):
    if n < 1:
        return 0
    if n == 1 or n == 2 or n == 3:
        return n
    res = 3
    pre = 2
    pre_pre = 1
    tmp1 = 0
    tmp2 = 0
    for i in range(4, n + 1):
        tmp1 = res
        tmp2 = pre
        res = res + pre_pre
        pre = tmp1
        pre_pre = tmp2
    return res


def c3(n: int):
    if n < 1:
        return 0
    if n == 1 or n == 2 or n == 3:
        return n
    base = [[1, 1, 0], [0, 0, 1], [1, 0, 0]]
    res = matrix_power(base, n - 3)
    return 3 * res[0][0] + 2 * res[1][0] + res[2][0]


if __name__ == '__main__':
    n = 19
    print(f1(n))
    print(f2(n))
    print(f3(n))
    print("===========")

    print(s1(n))
    print(s2(n))
    print(s3(n))
    print("===========")

    print(c1(n))
    print(c2(n))
    print(c3(n))
    print("===========")

