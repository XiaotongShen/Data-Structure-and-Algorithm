# -*- coding: utf-8 -*-

"""
@File: Code01_SplitSumClosed.py
@Author: Sarah Shen
@Time: 30/10/2022 11:42
"""
import random


def right(arr: [int]):
    if arr is None or len(arr) < 2:
        return 0
    sm = 0
    for num in arr:
        sm += num
    return process(arr, 0, int(sm / 2))


def process(arr: [int], idx: int, rest: int):
    if idx == len(arr):
        return 0
    else:
        p1 = process(arr, idx + 1, rest)
        p2 = 0
        if arr[idx] <= rest:
            p2 = arr[idx] + process(arr, idx + 1, rest - arr[idx])
        return max(p1, p2)


def split_sum_closed_dp(arr: [int]):
    if arr is None or len(arr) < 2:
        return 0
    sm = 0
    for num in arr:
        sm += num

    sm = int(sm / 2)
    n = len(arr)
    dp = [[0] * (sm + 1) for i in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for rest in range(sm + 1):
            p1 = dp[i + 1][rest]
            p2 = 0
            if arr[i] <= rest:
                p2 = arr[i] + dp[i + 1][rest - arr[i]]
            dp[i][rest] = max(p1, p2)
    return dp[0][sm]


def random_array(max_l: int, max_v: int):
    n = int(random.random() * max_l)
    arr = [0] * n
    for i in range(n):
        arr[i] = int(random.random() * max_v) + 1
    return arr


if __name__ == '__main__':
    max_len = 20
    max_value = 50
    test_times = 1000
    print('测试开始')
    for i in range(test_times):
        rand_arr = random_array(max_len, max_value)
        ans1 = right(rand_arr)
        ans2 = split_sum_closed_dp(rand_arr)
        if ans1 != ans2:
            print('Oops!')
            print(rand_arr)
            print(ans1, ans2)
            break
    print('测试结束')
