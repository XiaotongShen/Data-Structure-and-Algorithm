# -*- coding: utf-8 -*-

"""
@File: Code01_RobotWalk.py
@Author: Sarah Shen
@Time: 26/10/2022 10:04
"""


# 从暴力递归到动态规划
# 提议表述，一个长度为n的数组中，机器人从start走了k步走到aim，有多少种可能的走法
# 第一个方法，暴力递归的方法

def ways1(n: int, start: int, aim: int, k: int):
    # 写清边界条件
    if n < 2 or start < 1 or start > n or aim < 1 or aim > n or k < 1:
        return -1
    return process1(start, k, aim, n)


def process1(cur: int, rest: int, aim: int, n: int):
    # cur: 机器人当前来到的位置
    # rest：机器人剩下要走的步数
    # aim：最终的目标始终是aim
    # 可以走的位置1~n
    # 返回：机器人从cur出发，走过rest步知乎，最终填在aim的方法数是多少
    if rest == 0:
        return 1 if cur == aim else 0
    if cur == 1:
        return process1(2, rest - 1, aim, n)
    if cur == n:
        return process1(n - 1, rest - 1, aim, n)
    return process1(cur - 1, rest - 1, aim, n) + process1(cur + 1, rest - 1, aim, n)


# 定义一个简单的缓存，动态规划
def ways2(n: int, start: int, aim: int, k: int):
    if n < 2 or start < 1 or start > n or aim < 1 or aim > n or k < 1:
        return -1
    dp = [[-1] * (k + 1) for i in range(n + 1)]
    # dp就是缓存表
    # dp[cur][rest] == -1: 代表process2(cur, rest)之前没算过
    # dp[cur][rest] ！= -1: 代表process2(cur, rest)之前算过， 返回值，dp[cur][rest]
    return process2(start, k, aim, n, dp)


def process2(cur: int, rest: int, aim: int, n: int, dp):
    if dp[cur][rest] != -1:
        return dp[cur][rest]
    if rest == 0:
        ans = 1 if cur == aim else 0
    elif cur == 1:
        ans = process2(2, rest - 1, aim, n, dp)
    elif cur == n:
        ans = process2(n - 1, rest - 1, aim, n, dp)
    else:
        ans = process2(cur - 1, rest - 1, aim, n, dp) + process2(cur + 1, rest - 1, aim, n, dp)
    dp[cur][rest] = ans
    return ans


# 动态规划的方式求解
def ways3(n: int, start: int, aim: int, k: int):
    if n < 2 or start < 1 or start > n or aim < 1 or aim > n or k < 1:
        return -1
    dp = [[0] * (k + 1) for i in range(n + 1)]
    # dp是用来保存动态依赖的依赖表
    dp[aim][0] = 1  # 在剩余步骤是0的时候，aim位置的值是1
    for rest in range(1, k + 1):
        # 遍历每一步的情况
        # 如果位置在1，依赖2位置rest -1 步的结果
        dp[1][rest] = dp[2][rest - 1]
        # 正常情况下
        for cur in range(2, n):
            dp[cur][rest] = dp[cur - 1][rest - 1] + dp[cur + 1][rest - 1]
        dp[n][rest] = dp[n - 1][rest - 1]
    return dp[start][k]


if __name__ == '__main__':
    print(ways1(5, 2, 4, 6))
    print(ways2(5, 2, 4, 6))
    print(ways3(5, 2, 4, 6))
