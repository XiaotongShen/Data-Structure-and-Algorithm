# -*- coding: utf-8 -*-

"""
@File: Code02_AddShortestEnd.py
@Author: Sarah Shen
@Time: 03/11/2022 13:00
"""


def shortest_end(s: str):
    if s is None or len(s) == 0:
        return None
    ms = manacher_string(s)
    p_arr = [0] * len(ms)
    c = -1
    r = -1
    max_contains_end = -1
    for i in range(len(ms)):
        p_arr[i] = min(p_arr[2 * c - i], r - i) if r > i else 1
        while i + p_arr[i] < len(ms) and i - p_arr[i] > -1:
            if ms[i + p_arr[i]] == ms[i - p_arr[i]]:
                p_arr[i] += 1
            else:
                break
        if i + p_arr[i] > r:
            r = i + p_arr[i]
            c = i
        if r == len(ms):
            max_contains_end = p_arr[i]
            break
    res = [''] * (len(s) - max_contains_end + 1)
    for i in range(len(res)):
        res[len(res) - 1 - i] = ms[i * 2 + 1]
    ans = ''
    for i in range(len(res)):
        ans += res[i]
    return ans


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


if __name__ == '__main__':
    str1 = "abcd123321"
    print(shortest_end(str1))
