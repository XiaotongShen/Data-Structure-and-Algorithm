# -*- coding: utf-8 -*-

"""
@File: Code02_MinCoinsNoLimit.py
@Author: Sarah Shen
@Time: 29/10/2022 13:24
"""
import sys
import random


def min_coins(arr: list, aim: int):
    return process(arr, 0, aim)


def process(arr: list, idx: int, rest: int):
    """
    arr[idx...]面值，每种面值张数自由选择
    搞出rest正好这么多钱，返回最小张数
    拿sys.maxsize标记怎么都搞定不了
    """
    if idx == len(arr):
        return 0 if rest == 0 else sys.maxsize
    else:
        ans = sys.maxsize
        note = 0
        while note * arr[idx] <= rest:
            nxt = process(arr, idx + 1, rest - note * arr[idx])
            if next != sys.maxsize:
                ans = min(ans, note + nxt)
            note += 1
        return ans


def dp1(arr: list, aim: int):
    if aim == 0:
        return 0
    n = len(arr)
    dp = [[0] * (aim + 1) for i in range(n + 1)]
    # base case, 只有n,0位置是0， 其他位置都是系统最大值
    dp[n][0] = 0
    for j in range(1, aim + 1):
        dp[n][j] = sys.maxsize
    for idx in range(n - 1, -1, -1):
        for rest in range(aim + 1):
            ans = sys.maxsize
            note = 0
            while note * arr[idx] <= rest:
                nxt = dp[idx + 1][rest - note * arr[idx]]
                if next != sys.maxsize:
                    ans = min(ans, note + nxt)
                note += 1
            dp[idx][rest] = ans
    return dp[0][aim]


def dp2(arr: list, aim: int):
    if aim == 0:
        return 0
    n = len(arr)
    dp = [[0] * (aim + 1) for i in range(n + 1)]
    dp[n][0] = 0
    for j in range(1, aim + 1):
        dp[n][j] = sys.maxsize
    for idx in range(n - 1, -1, -1):
        for rest in range(aim + 1):
            dp[idx][rest] = dp[idx + 1][rest]
            if rest - arr[idx] >= 0 and dp[idx][rest - arr[idx]] != sys.maxsize:
                dp[idx][rest] = min(dp[idx][rest], dp[idx][rest - arr[idx]] + 1)
    return dp[0][aim]


def random_array(max_l: int, max_v: int):
    n = int(random.random() * max_l)
    arr = [0] * n
    has = [False] * (max_v + 1)
    for i in range(n):
        arr[i] = int(random.random() * max_v) + 1
        while has[arr[i]]:
            arr[i] = int(random.random() * max_v) + 1
        has[arr[i]] = True
    return arr


if __name__ == '__main__':
    max_len = 20
    max_value = 30
    test_times = 1000
    print('测试开始')
    for i in range(test_times):
        rand_arr = random_array(max_len, max_value)
        rand_aim = int(random.random() * max_value)
        ans1 = min_coins(rand_arr, rand_aim)
        ans2 = dp1(rand_arr, rand_aim)
        ans3 = dp2(rand_arr, rand_aim)
        if ans1 != ans2 or ans1 != ans3:
            print('Oops!')
            print(rand_arr, rand_aim)
            print(ans1, ans2, ans3)
            break
    print('测试结束')
