# -*- coding: utf-8 -*-

"""
@File: Code02_CoinsWayEveryPaperDifferent.py
@Author: Sarah Shen
@Time: 29/10/2022 13:24
"""
import random


def coin_ways(arr: list, aim: int):
    return process(arr, 0, aim)


def process(arr: list, idx: int, rest: int):
    if rest < 0:
        return 0
    if idx == len(arr):
        return 1 if rest == 0 else 0
    else:
        return process(arr, idx + 1, rest) + process(arr, idx + 1, rest - arr[idx])


def coin_ways_dp(arr: list, aim: int):
    if aim == 0:
        return 1
    n = len(arr)
    dp = [[0] * (aim + 1) for i in range(n + 1)]
    dp[n][0] = 1
    for idx in range(n - 1, -1, -1):
        for rest in range(aim + 1):
            dp[idx][rest] = dp[idx + 1][rest] + (dp[idx + 1][rest - arr[idx]] if rest - arr[idx] >= 0 else 0)
    return dp[0][aim]


# for test
def random_array(max_len: int, max_v: int):
    len_n = int(random.random() * max_len)
    a = [0] * len_n
    for i in range(len_n):
        a[i] = int(random.random() * max_v) + 1
    return a


if __name__ == '__main__':
    ml = 20
    mv = 30
    test_time = 100000
    print('测试开始')
    for i in range(test_time):
        rand_arr = random_array(ml, mv)
        rand_aim = int(random.random() * mv)
        ans1 = coin_ways(rand_arr, rand_aim)
        ans2 = coin_ways_dp(rand_arr, rand_aim)
        if ans1 != ans2:
            print(rand_arr)
            print(rand_aim)
            print(ans1)
            print(ans2)
            print('Oops!')
            break
    print('测试结束')
