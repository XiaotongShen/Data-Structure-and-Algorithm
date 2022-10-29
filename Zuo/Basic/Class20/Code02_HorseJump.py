# -*- coding: utf-8 -*-

"""
@File: Code02_HorseJump.py
@Author: Sarah Shen
@Time: 29/10/2022 13:23
"""


# 当前的位置是(x,y)
# 还剩下rest步需要跳
# 跳完rest步，正好跳到(a, b)的方法数是多少？
# 10*9
def jump(a: int, b: int, k: int):
    return process(0, 0, k, a, b)


def process(x: int, y: int, rest: int, a: int, b: int):
    if x < 0 or x > 9 or y < 0 or y > 8:
        return 0
    if rest == 0:
        return 1 if x == a and y == b else 0
    ways = process(x + 2, y + 1, rest - 1, a, b)
    ways += process(x + 1, y + 2, rest - 1, a, b)
    ways += process(x - 1, y + 2, rest - 1, a, b)
    ways += process(x - 2, y + 1, rest - 1, a, b)
    ways += process(x - 2, y - 1, rest - 1, a, b)
    ways += process(x - 1, y - 2, rest - 1, a, b)
    ways += process(x + 1, y - 2, rest - 1, a, b)
    ways += process(x + 2, y - 1, rest - 1, a, b)

    return ways


def jump_dp(a: int, b: int, k: int):
    dp = [[[0] * (k + 1) for i in range(9)] for j in range(10)]
    dp[a][b][0] = 1
    for rest in range(1, k + 1):
        for x in range(10):
            for y in range(9):
                ways = pick(dp, x + 2, y + 1, rest - 1)
                ways += pick(dp, x + 1, y + 2, rest - 1)
                ways += pick(dp, x - 1, y + 2, rest - 1)
                ways += pick(dp, x - 2, y + 1, rest - 1)
                ways += pick(dp, x - 2, y - 1, rest - 1)
                ways += pick(dp, x - 1, y - 2, rest - 1)
                ways += pick(dp, x + 1, y - 2, rest - 1)
                ways += pick(dp, x + 2, y - 1, rest - 1)
                dp[x][y][rest] = ways

    return dp[0][0][k]


def pick(dp, x: int, y: int, rest: int):
    if x < 0 or x > 9 or y < 0 or y > 8:
        return 0
    return dp[x][y][rest]


if __name__ == '__main__':
    x = 7
    y = 7
    step = 10
    print(jump(x, y, step))
    print(jump_dp(x, y, step))
