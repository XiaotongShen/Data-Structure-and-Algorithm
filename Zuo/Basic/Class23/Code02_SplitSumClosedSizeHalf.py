# -*- coding: utf-8 -*-

"""
@File: Code02_SplitSumClosedSizeHalf.py
@Author: Sarah Shen
@Time: 30/10/2022 13:49
"""
import random


def right(arr: [int]):
    if arr is None or len(arr) < 2:
        return 0
    s = 0
    for num in arr:
        s += num
    if (len(arr) % 2) == 0:
        return process(arr, 0, int(len(arr) / 2), int(s / 2))
    else:
        return max(process(arr, 0, int(len(arr) / 2), int(s / 2)), process(arr, 0, int(len(arr) / 2) + 1, int(s / 2)))


def process(arr: [int], idx: int, picks: int, rest: int):
    """ arr[i...]自由选择，挑选的个数一定要是picks个，累加和<= rest, 离rest最近的返回 """
    if idx == len(arr):
        return 0 if picks == 0 else -1
    else:
        # 不是用arr[idx]这个数
        p1 = process(arr, idx + 1, picks, rest)
        # 就是要是用arr[idx]这个数
        p2 = -1
        nxt = -1
        if arr[idx] <= rest:
            nxt = process(arr, idx + 1, picks - 1, rest - arr[idx])
        if nxt != -1:
            p2 = arr[idx] + nxt
        return max(p1, p2)


def dp1(arr: [int]):
    if arr is None or len(arr) < 2:
        return 0
    s = 0
    for num in arr:
        s += num
    s = int(s / 2)
    n = len(arr)
    m = int((n + 1) / 2)
    dp = [[[0] * (s + 1) for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            for k in range(s + 1):
                dp[i][j][k] = -1
    for rest in range(s + 1):
        dp[n][0][rest] = 0
    for i in range(n - 1, -1, -1):
        for picks in range(m + 1):
            for rest in range(s + 1):
                p1 = dp[i + 1][picks][rest]
                p2 = -1
                nxt = -1
                if picks - 1 >= 0 and arr[i] <= rest:
                    nxt = dp[i + 1][picks - 1][rest - arr[i]]
                if nxt != -1:
                    p2 = arr[i] + nxt
                dp[i][picks][rest] = max(p1, p2)
    if (len(arr) % 2) == 0:
        return dp[0][int(len(arr) / 2)][s]
    else:
        return max(dp[0][int(len(arr) / 2)][s], dp[0][int(len(arr) / 2) + 1][s])


def random_array(max_l: int, max_v: int):
    n = int(random.random() * max_l)
    arr = [0] * n
    for i in range(n):
        arr[i] = int(random.random() * max_v)
    return arr


if __name__ == '__main__':
    max_len = 19
    max_value = 50
    test_times = 100
    print('测试开始')
    for i in range(test_times):
        rand_arr = random_array(max_len, max_value)
        ans1 = right(rand_arr)
        ans2 = dp1(rand_arr)
        if ans1 != ans2:
            print('Oops!')
            print(rand_arr)
            print(ans1, ans2)
            break
    print('测试完成')



