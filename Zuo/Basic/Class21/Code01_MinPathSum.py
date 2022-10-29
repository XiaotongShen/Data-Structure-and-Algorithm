# -*- coding: utf-8 -*-

"""
@File: Code01_MinPathSum.py
@Author: Sarah Shen
@Time: 29/10/2022 13:24
"""
import random


# 题目
# 给定一个matrix,从左上走到右下的最小路径
def min_path_sum1(m: [list]):
    """ 严格表结构的动态规划过程 """
    if m is None or len(m) == 0 or m[0] is None or len(m[0]) == 0:
        return 0
    row = len(m)
    col = len(m[0])
    dp = [[0] * col for i in range(row)]
    dp[0][0] = m[0][0]
    for j in range(1, col):
        # 填写第一行
        dp[0][j] = dp[0][j - 1] + m[0][j]
    for i in range(1, row):
        # 填写第一列
        dp[i][0] = dp[i - 1][0] + m[i][0]
    for i in range(1, row):
        for j in range(1, col):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + m[i][j]
    return dp[row - 1][col - 1]


def min_path_sum2(m: [list]):
    """ 压缩数组的动态规划过程 """
    if m is None or len(m) == 0 or m[0] is None or len(m[0]) == 0:
        return 0
    row = len(m)
    col = len(m[0])
    dp = [0] * col
    dp[0] = m[0][0]
    for j in range(1, col):
        dp[j] = dp[j - 1] + m[0][j]
    for i in range(1, row):
        dp[0] += m[i][0]
        for j in range(1, col):
            dp[j] = min(dp[j - 1], dp[j]) + m[i][j]
    return dp[col - 1]


# for test
def generate_random_matrix(row_size: int, col_size: int):
    if row_size < 0 or col_size < 0:
        return None
    res = [[0] * col_size for i in range(row_size)]
    for i in range(len(res)):
        for j in range(len(res[0])):
            res[i][j] = int(random.random() * 100)
    return res


if __name__ == '__main__':
    r_size = 10
    c_size = 10
    ma = generate_random_matrix(r_size, c_size)
    print(min_path_sum1(ma))
    print(min_path_sum2(ma))
