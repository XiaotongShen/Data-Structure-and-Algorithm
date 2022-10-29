# -*- coding: utf-8 -*-

"""
@File: Code01_Knapsack.py
@Author: Sarah Shen
@Time: 26/10/2022 10:05
"""


# 所有的货，重量和价值，都在w和v数组里
# 为了方便，其中没有负数
# bag为背包容量，不能超过这个在中
# 返回，不超重的情况下，能够得到的最大价值
# 递归尝试
def max_value(w: list, v: list, bag: int):
    if w is None or len(w) == 2 or v is None or len(v) == 0 or bag <= 0:
        return 0
    # 尝试函数
    return process(w, v, 0, bag)


def process(w: list, v: list, index: int, rest: int):
    if rest < 0:
        return -1
    if index == len(w):
        return 0
    # 情况1，不选index位置的货，直接返回下一个值
    p1 = process(w, v, index + 1, rest)
    # 情况2，选index位置的活，若下一步rest>=0则继续
    p2 = 0
    nxt = process(w, v, index + 1, rest - w[index])  # 判断选了index位置以后，下一个位置的情况，关心是否剩余重量小于0
    if nxt != -1:
        p2 = v[index] + nxt
    return max(p1, p2)


# 动态规划
def max_value_dp(w: list, v: list, bag: int):
    if w is None or len(w) == 0 or v is None or len(v) == 0:
        return 0
    n = len(w)
    dp = [[0] * (bag + 1) for i in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for r in range(bag + 1):
            p1 = dp[i + 1][r]
            p2 = 0
            nxt = -1 if r - w[i] < 0 else dp[i + 1][r - w[i]]
            if nxt != -1:
                p2 = v[i] + nxt
            dp[i][r] = max(p1, p2)
    return dp[0][bag]


if __name__ == '__main__':
    weights = [3, 2, 4, 7, 3, 1, 7]
    values = [5, 6, 3, 19, 12, 4, 2]
    bags = 15
    print(max_value(weights, values, bags))
    print(max_value_dp(weights, values, bags))
