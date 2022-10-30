# -*- coding: utf-8 -*-

"""
@File: Code03_CoinsWayNoLimit.py
@Author: Sarah Shen
@Time: 29/10/2022 13:24
"""
import random


def coins_way(arr: list, aim: int):
    if arr is None or len(arr) == 0 or aim < 0:
        return 0
    return process(arr, 0, aim)


def process(arr: list, idx: int, rest: int):
    if idx == len(arr):
        return 1 if rest == 0 else 0
    ways = 0
    note = 0
    while note * arr[idx] <= rest:
        ways += process(arr, idx + 1, rest - (note * arr[idx]))
        note += 1
    return ways


def coins_way_dp1(arr: list, aim: int):
    if arr is None or len(arr) == 0 or aim < 0:
        return 0
    n = len(arr)
    dp = [[0] * (aim + 1) for i in range(n + 1)]
    dp[n][0] = 1
    for idx in range(n - 1, -1, -1):
        for rest in range(aim + 1):
            ways = 0
            note = 0
            while note * arr[idx] <= rest:
                ways += dp[idx + 1][rest - (note * arr[idx])]
                note += 1
            dp[idx][rest] = ways
    return dp[0][aim]


def coins_way_dp2(arr: list, aim: int):
    if arr is None or len(arr) == 0 or aim < 0:
        return 0
    n = len(arr)
    dp = [[0] * (aim + 1) for i in range(n + 1)]
    dp[n][0] = 1
    for idx in range(n - 1, -1, -1):
        for rest in range(aim + 1):
            dp[idx][rest] = dp[idx + 1][rest]
            if rest - arr[idx] >= 0:
                dp[idx][rest] += dp[idx][rest - arr[idx]]
    return dp[0][aim]


def random_arr(max_l: int, max_v: int):
    arr_len = int(random.random() * max_l)
    rand_arr = random.sample(range(1, max_v + 1), arr_len)
    return rand_arr


if __name__ == '__main__':
    max_len = 10
    max_value = 30
    test_time = 10000
    print('测试开始')
    for i in range(test_time):
        arr = random_arr(max_len, max_value)
        rand_aim = int(random.random() * max_value)
        # print(arr, rand_aim)
        ans1 = coins_way(arr, rand_aim)
        ans2 = coins_way_dp1(arr, rand_aim)
        ans3 = coins_way_dp2(arr, rand_aim)
        if ans1 != ans2 or ans2 != ans3:
            print('Oops!')
            print(arr)
            print(rand_aim)
            print(ans1)
            print(ans2)
            print(ans3)
            break
    print('测试结束')
