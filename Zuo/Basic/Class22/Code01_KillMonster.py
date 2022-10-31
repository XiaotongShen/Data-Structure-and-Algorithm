# -*- coding: utf-8 -*-

"""
@File: Code01_KillMonster.py
@Author: Sarah Shen
@Time: 29/10/2022 13:24
"""
import random


def right(n: int, m: int, k: int):
    """
    怪兽有k点血
    英雄每砍一刀可以掉0~m点血
    求砍n刀后，怪兽死掉的概率
    """
    if n < 1 or m < 1 or k < 1:
        return 0
    all = pow(m + 1, k)
    kill = process(n, m, k)
    return kill / all


def process(hp: int, m: int, times: int):
    """
    times：还可以砍多少到
    hurt：每刀最大的伤害
    hp：怪兽剩余的血值
    """
    if times == 0:
        return 1 if hp <= 0 else 0
    if hp <= 0:
        return pow((m + 1), times)
    ways = 0
    for i in range(m+1):
        ways += process(hp - i, m, times - 1)
    return ways


def dp1(n: int, m: int, k: int):
    """
    可以砍k到，
    每刀可以砍掉0~m点血，
    怪兽有n滴血
    """
    if n < 1 or m < 1 or k < 1:
        return 0
    all = pow((m + 1), k)
    dp = [[0] * (n + 1) for i in range(k + 1)]
    dp[0][0] = 1
    for times in range(1, k + 1):
        dp[times][0] = pow((m + 1), times)
        for hp in range(1, n + 1):
            ways = 0
            for hurt in range(m + 1):
                if hp - hurt >= 0:
                    ways += dp[times - 1][hp - hurt]
                else:
                    ways += pow(m + 1, times - 1)

            dp[times][hp] = ways
    kill = dp[k][n]
    return kill / all


def dp2(n: int, m: int, k: int):
    if n < 1 or m < 1 or k < 1:
        return 0
    all = pow(m + 1, k)
    dp = [[0] * (n + 1) for i in range(k + 1)]
    dp[0][0] = 1
    for times in range(1, k + 1):
        dp[times][0] = pow(m + 1, times)
        for hp in range(1, n + 1):
            dp[times][hp] = dp[times][hp - 1] + dp[times - 1][hp]
            if hp - 1 - m >= 0:
                dp[times][hp] -= dp[times - 1][hp - 1 - m]
            else:
                dp[times][hp] -= pow(m + 1, times - 1)
    kill = dp[k][n]
    return kill / all


if __name__ == '__main__':
    n_max = 10
    m_max = 10
    k_max = 10
    test_times = 200
    print('测试开始')
    for i in range(test_times):
        rand_n = int(random.random() * n_max)
        rand_m = int(random.random() * m_max)
        rand_k = int(random.random() * k_max)
        ans1 = right(rand_n, rand_m, rand_k)
        ans2 = dp1(rand_n, rand_m, rand_k)
        ans3 = dp2(rand_n, rand_m, rand_k)
        if ans1 != ans2 or ans2 != ans3:
            print('Oops!')
            print(rand_n, rand_m, rand_k)
            print(ans1, ans2, ans3)
            break
    print('测试结束')
