# -*- coding: utf-8 -*-

"""
@File: Code05_BobDie.py
@Author: Sarah Shen
@Time: 29/10/2022 13:24
"""


def live_possibility1(row: int, col: int, k: int, n: int, m: int):
    return process(row, col, k, n, m) / pow(4, k)


def process(row: int, col: int, rest: int, n: int, m: int):
    """
    在n*m的棋盘中，bob在row, col位置，还有rest步要走
    走完了如果还在棋盘中就获得1个生存点，返回总得生存点数
    """
    if row < 0 or row == n or col < 0 or col == m:  # 越界，超过棋盘范围的情况
        return 0
    if rest == 0:  # 走完了，但是没有出棋盘，获得1个生存点
        return 1
    up = process(row - 1, col, rest - 1, n, m)  # 还在棋盘中，还有步数要走
    down = process(row + 1, col, rest - 1, n, m)
    left = process(row, col - 1, rest - 1, n, m)
    right = process(row, col + 1, rest - 1, n, m)
    return up + down + left + right


def live_possibility2(row: int, col: int, k: int, n: int, m: int):
    dp = [[[0] * (k + 1) for i in range(m)] for j in range(n)]
    # base case，当rest == 0 的时候，获得一个生存点
    for i in range(n):
        for j in range(m):
            dp[i][j][0] = 1
            # 从下往上填写3为dp表
    for rest in range(1, k + 1):
        for r in range(n):
            for c in range(m):
                dp[r][c][rest] = pick(dp, n, m, r - 1, c, rest - 1)
                dp[r][c][rest] += pick(dp, n, m, r + 1, c, rest - 1)
                dp[r][c][rest] += pick(dp, n, m, r, c - 1, rest - 1)
                dp[r][c][rest] += pick(dp, n, m, r, c + 1, rest - 1)
    return dp[row][col][k] / pow(4, k)


def pick(dp, n: int, m: int, r: int, c: int, rest: int):
    if r < 0 or r == n or c < 0 or c == m:
        return 0
    return dp[r][c][rest]


if __name__ == '__main__':
    print(live_possibility1(6, 6, 10, 50, 50))
    print(live_possibility2(6, 6, 10, 50, 50))
