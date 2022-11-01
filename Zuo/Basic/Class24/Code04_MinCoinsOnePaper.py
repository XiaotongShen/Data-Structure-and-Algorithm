# -*- coding: utf-8 -*-

"""
@File: Code04_MinCoinsOnePaper.py
@Author: Sarah Shen
@Time: 31/10/2022 22:46
"""
import sys


# 暴力递归的方法
def min_coins(arr: [int], aim: int):
    return process(arr, 0, aim)


def process(arr: [int], idx: int, rest: int):
    if rest < 0:
        return sys.maxsize
    if idx == len(arr):
        return 0 if rest == 0 else sys.maxsize
    else:
        p1 = process(arr, idx + 1, rest)
        p2 = process(arr, idx + 1, rest - arr[idx])
        if p1 != sys.maxsize:
            p2 += 1
        return min(p1, p2)


# 严格表结构的方法
def dp1(arr: [int], aim: int):
    if aim == 0:
        return 0
    n = len(arr)
    dp = [[0] * (aim + 1) for i in range(n + 1)]
    dp[n][0] = 0
    for j in range(1, aim + 1):
        dp[n][j] = sys.maxsize
    for idx in range(n - 1, -1, -1):
        for rest in range(aim + 1):
            p1 = dp[idx + 1][rest]
            p2 = dp[idx + 1][rest - arr[idx]] if rest - arr[idx] >= 0 else sys.maxsize
            if p2 != sys.maxsize:
                p2 += 1
            dp[idx][rest] = min(p1, p2)
    return dp[0][aim]


class Info:

    def __init__(self, v: [int], n: [int]):
        self.value = v
        self.notes = n


def get_info(arr: [int]):
    counts = dict()
    for v in arr:
        if not counts.keys().__contains__(v):
            counts[v] = 1
        else:
            counts[v] += 1
    n = len(counts)
    values = [0] * n
    notes = [0] * n
    idx = 0
    for k, v in counts.items():
        values[idx] = k
        notes[idx] = v
        idx += 1
    return Info(values, notes)


def dp2(arr: [int], aim: int):
    if aim == 0:
        return 0
    info = get_info(arr)
    values = info.value
    notes = info.notes
    n = len(values)
    dp = [[0] * (aim + 1) for i in range(n + 1)]
    dp[n][0] = 0
    for j in range(aim + 1):
        dp[n][j] = sys.maxsize
    for idx in range(n - 1, -1, -1):
        for rest in range(aim + 1):
            dp[idx][rest] = dp[idx + 1][rest]  # 完全没选values[idx]的情况
            note = 1
            while note * values[idx] <= aim and note <= notes[idx]:
                if rest - note * values[idx] >= 0 and dp[idx + 1][rest - note * values[idx] != sys.maxsize]:
                    dp[idx][rest] = min(dp[idx][rest], note + dp[idx + 1][rest - note * values[idx]])
    return dp[0][aim]


def dp3(arr:[int], aim:int):
    if aim == 0:
        return 0
    info = get_info(arr)
    v = info.value
    nt = info.notes
    n = len(v)
    dp = [[0] * (aim+1) for i in range(n+1)]
    dp[n][0] = 0
    for j in range(aim+1):
        dp[n][j] = sys.maxsize
    # 虽然嵌套了很多魂环，但是时间复杂度为O(货币种数 * aim）
    # 因为用了窗口内最小值的更新结构
    for i in range(n-1, -1, -1):
        for mod in range(min(aim+1, v[i])):
            # TODO

if __name__ == '__main__':
    a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
    b = get_info(a)
    print(b.value)
    print(b.notes)
