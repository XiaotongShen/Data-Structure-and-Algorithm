# -*- coding: utf-8 -*-

"""
@File: Code01_KMP.py
@Author: Sarah Shen
@Time: 03/11/2022 12:59
"""
import random


def get_index_of(s1: str, s2: str):
    if s1 is None or s2 is None or len(s2) < 1 or len(s1) < len(s2):
        return -1
    str1 = list(s1)
    str2 = list(s2)
    x = 0
    y = 0
    nxt = get_next_array(str2)
    while x < len(str1) and y < len(str2):
        if str1[x] == str2[y]:
            x += 1
            y += 1
        elif nxt[y] == -1:
            x += 1
        else:
            y = nxt[y]
    return x - y if len(str2) == y else -1


def get_next_array(str2: [str]):
    if len(str2) == 1:
        return [-1]
    nxt = [0] * len(str2)
    nxt[0] = -1
    nxt[1] = 0
    i = 2  # 目前在哪个位置上求next数组的值
    cn = 0  # 当前是哪个位置的值在和i-1位置的字符比较
    while i < len(nxt):
        if str2[i - 1] == str2[cn]:
            cn += 1
            nxt[i] = cn
            i += 1
        elif cn > 0:
            cn = nxt[cn]
        else:
            nxt[i] = 0
            i += 1
    return nxt


def get_random_string(possibilities: int, size: int):
    n = int(random.random() * size + 1)
    ans = ''
    for i in range(n):
        ans += chr(int(random.random() * possibilities) + ord('a'))
    return ans


if __name__ == '__main__':
    pos = 5
    str_size = 20
    match_size = 5
    test_times = 50000
    print("test begin")
    for i in range(test_times):
        rand_str = get_random_string(pos, str_size)
        rand_match = get_random_string(pos, match_size)
        ans1 = rand_str.find(rand_match)
        ans2 = get_index_of(rand_str, rand_match)
        if ans1 != ans2:
            print('Oops!')
            print(rand_str, rand_match)
            print(ans1, ans2)
    print('test finish')
