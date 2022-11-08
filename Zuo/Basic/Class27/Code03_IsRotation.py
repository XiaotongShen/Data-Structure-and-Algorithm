# -*- coding: utf-8 -*-

"""
@File: Code03_IsRotation.py
@Author: Sarah Shen
@Time: 03/11/2022 12:59
"""


def is_rotation(a: str, b: str):
    if a is None or b is None or len(a) != len(b):
        return False
    b2 = b + b
    return get_index_of(b2, a) != -1


def get_index_of(s: str, m: str):
    if len(s) < len(m):
        return -1
    ss = list(s)
    ms = list(m)
    si = 0
    mi = 0
    nxt = get_next_array(ms)
    while si < len(ss) and mi < len(ms):
        if ss[si] == ms[mi]:
            si += 1
            mi += 1
        elif nxt[mi] == -1:
            si += 1
        else:
            mi = nxt[mi]
    return si - mi if len(ms) == mi else -1


def get_next_array(ms: [str]):
    if len(ms) == 1:
        return [-1]
    nxt = [0] * len(ms)
    nxt[0] = -1
    nxt[1] = 0
    pos = 2
    cn = 0
    while pos < len(nxt):
        if ms[pos - 1] == ms[cn]:
            cn += 1
            nxt[pos] = cn
            pos += 1
        elif cn > 0:
            cn = nxt[cn]
        else:
            nxt[pos] = 0
            pos += 1
    return nxt


if __name__ == '__main__':
    str1 = 'yunzuocheng'
    str2 = 'zuochengyun'
    print(is_rotation(str1, str2))
