# -*- coding: utf-8 -*-

"""
@File: Code01_Manacher.py
@Author: Sarah Shen
@Time: 03/11/2022 12:59
"""
import random
import sys


def manacher(s: str):
    if s is None or len(s) == 0:
        return 0
        # "12132" -> "#1#2#1#3#2#"
    ms = manacher_string(s)
    # 回文半径的大小
    p_arr = [0] * len(ms)
    c = -1  # 最右回文序列的中心位置
    r = -1  # r代表最有的扩成功的位置
    max_v = -sys.maxsize-1
    for i in range(len(ms)):
        # r第一个违规的位置是i > r
        # i位置扩出来的答案，i位置扩的区域，至少是多大
        p_arr[i] = min(p_arr[2 * c - i], r - i) if r > i else 1
        while i + p_arr[i] < len(ms) and i - p_arr[i] > -1:
            if ms[i + p_arr[i]] == ms[i - p_arr[i]]:
                p_arr[i] += 1
            else:
                break
        if i + p_arr[i] > r:
            r = i + p_arr[i]
            c = i
        max_v = max(max_v, p_arr[i])
    return max_v - 1


def manacher_string(s: str):
    res = ''
    n = len(s) * 2 + 1
    idx = 0
    for i in range(n):
        if (i & 1) == 0:
            res += '#'
        else:
            res += s[idx]
            idx += 1
    return res


def right(s: str):
    if s is None or len(s) == 0:
        return 0
    ms = manacher_string(s)
    max_v = 0
    for i in range(len(ms)):
        l = i - 1
        r = i + 1
        while l >= 0 and r < len(ms) and ms[l] == ms[r]:
            l -= 1
            r += 1
        max_v = max(max_v, r - l - 1)
    return int(max_v / 2)


def get_random_string(possibilities: int, size: int):
    ans = ''
    n = int(random.random() * size + 1)
    for i in range(n):
        ans += chr(int(random.random() * possibilities) + ord('a'))
    return ans


if __name__ == '__main__':
    pos = 5
    str_size = 20
    test_times = 50000
    print('test begin')
    for i in range(test_times):
        rand_s = get_random_string(pos, str_size)
        ans1 = manacher(rand_s)
        ans2 = right(rand_s)
        if ans1 != ans2:
            print('Oops!')
            print(rand_s)
            print(ans1, ans2)
            break
    print('test finish')
