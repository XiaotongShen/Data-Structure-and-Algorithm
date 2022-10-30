# -*- coding: utf-8 -*-

"""
@File: Code04_CoinsWaySameValueSamePaper.py
@Author: Sarah Shen
@Time: 29/10/2022 13:24
"""
import random


class Info:

    def __init__(self, v: list, n: list):
        self.values = v
        self.notes = n


def get_info(arr: list):
    counts = dict()
    for value in arr:
        if not counts.keys().__contains__(value):
            counts[value] = 1
        else:
            counts[value] += 1
    values = []
    notes = []
    for k, v in counts.items():
        values.append(k)
        notes.append(v)
    return Info(values, notes)


def coins_way(arr: list, aim: int):
    if arr is None or len(arr) == 0 or aim < 0:
        return 0
    info = get_info(arr)
    return process(info.values, info.notes, 0, aim)


def process(values: list, notes: list, idx: int, rest: int):
    if idx == len(values):
        return 1 if rest == 0 else 0
    ways = 0
    note = 0
    while note * values[idx] <= rest and note <= notes[idx]:
        ways += process(values, notes, idx + 1, rest - (note * values[idx]))
        note += 1
    return ways


def coins_way_dp1(arr: list, aim: int):
    if arr is None or len(arr) == 0 or aim < 0:
        return 0
    info = get_info(arr)
    values = info.values
    notes = info.notes
    n = len(values)
    dp = [[0] * (aim + 1) for i in range(n + 1)]
    dp[n][0] = 1
    for idx in range(n - 1, -1, -1):
        for rest in range(aim + 1):
            ways = 0
            note = 0
            while note * values[idx] <= rest and note <= notes[idx]:
                ways += dp[idx + 1][rest - note * values[idx]]
                note += 1
            dp[idx][rest] = ways
    return dp[0][aim]


def coins_way_dp2(arr: list, aim: int):
    if arr is None or len(arr) == 0 or aim < 0:
        return 0
    info = get_info(arr)
    values = info.values
    notes = info.notes
    n = len(values)
    dp = [[0] * (aim + 1) for i in range(n + 1)]
    dp[n][0] = 1
    for idx in range(n - 1, -1, -1):
        for rest in range(aim + 1):
            dp[idx][rest] = dp[idx + 1][rest]
            if rest - values[idx] >= 0:
                dp[idx][rest] += dp[idx][rest - values[idx]]
            if rest - values[idx] * (notes[idx] + 1) >= 0:
                dp[idx][rest] -= dp[idx + 1][rest - values[idx] * (notes[idx] + 1)]
    return dp[0][aim]


def random_arr(max_l: int, max_v: int):
    arr_len = int(random.random() * max_l)
    arr = [0] * arr_len
    for i in range(arr_len):
        arr[i] = int(random.random() * max_v) + 1
    return arr


if __name__ == '__main__':
    max_len = 10
    max_value = 20
    test_times = 10000
    print('测试开始')
    for i in range(test_times):
        rand_arr = random_arr(max_len, max_value)
        rand_aim = int(random.random() * max_value) + 1
        ans1 = coins_way(rand_arr, rand_aim)
        ans2 = coins_way_dp1(rand_arr, rand_aim)
        ans3 = coins_way_dp2(rand_arr, rand_aim)
        if ans1 != ans2 or ans2 != ans3:
            print('Oops!')
            print(rand_arr, rand_aim)
            print(ans1, ans2, ans3)
            break
    print('测试结束')
