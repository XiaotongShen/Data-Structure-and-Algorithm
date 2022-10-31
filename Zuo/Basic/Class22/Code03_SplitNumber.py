# -*- coding: utf-8 -*-

"""
@File: Code03_NQueens.py
@Author: Sarah Shen
@Time: 29/10/2022 13:24
"""


def split_num(n: int):
    if n < 0:
        return 0
    if n == 1:
        return 1
    return process(1, n)


def process(pre: int, rest: int):
    if rest == 0:
        return 1
    if pre > rest:
        return 0
    ways = 0
    for first in range(pre, rest + 1):
        ways += process(first, rest - first)
    return ways


def dp1(n: int):
    if n < 0:
        return 0
    if n == 1:
        return 1
    dp = [[0] * (n + 1) for i in range(n + 1)]
    for pre in range(n + 1):
        dp[pre][0] = 1
        dp[pre][pre] = 1
    for pre in range(n - 1, 0, -1):
        for rest in range(pre + 1, n + 1):
            ways = 0
            for first in range(pre, rest + 1):
                ways += dp[first][rest - first]
            dp[pre][rest] = ways
    return dp[1][n]


def dp2(n: int):
    if n < 0:
        return 0
    if n == 1:
        return 1
    dp = [[0] * (n + 1) for i in range(n + 1)]
    for pre in range(1, n + 1):
        dp[pre][0] = 1
        dp[pre][pre] = 1
    for pre in range(n - 1, 0, -1):
        for rest in range(pre +1, n + 1):
            dp[pre][rest] = dp[pre + 1][rest]
            dp[pre][rest] += dp[pre][rest - pre]
    return dp[1][n]


if __name__ == '__main__':
    test = 39
    ans1 = split_num(test)
    ans2 = dp1(test)
    ans3 = dp2(test)
    print(ans1, ans2, ans3)
