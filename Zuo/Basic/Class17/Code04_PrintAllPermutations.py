# -*- coding: utf-8 -*-

"""
@File: Code04_PrintAllPermutations.py
@Author: Sarah Shen
@Time: 26/10/2022 10:04
"""


# 打印字符串的所有全排列可能
def permutation1(s: str):
    ans = list()
    if s is None or len(s) == 0:
        return ans
    str_list = list(s)
    rest = list()
    for c in str_list:
        rest.append(c)
    path = ""
    f(rest, path, ans)
    return ans


def f(rest, path: str, ans: list):
    if len(rest) == 0:
        ans.append(path)
    else:
        n = len(rest)
        for i in range(n):
            cur = rest[i]
            rest.remove(cur)
            f(rest, path + cur, ans)
            rest.insert(i, cur)  # 恢复现场


def permutation2(s: str):
    ans = list()
    if s is None or len(s) == 0:
        return ans
    str_list = list(s)
    g1(str_list, 0, ans)
    return ans


def g1(s_list: list, index: int, ans: list):
    if index == len(s_list):
        ans.append(str(s_list))
    else:
        for i in range(index, len(s_list)):
            swap(s_list, index, i)
            g1(s_list, index + 1, ans)
            swap(s_list, index, i)


def permutation3(s: str):
    ans = list()
    if s is None or len(s) == 0:
        return ans
    str_list = list(s)
    g2(str_list, 0, ans)
    return ans


def g2(s_list: list, index: int, ans: list):
    if index == len(s_list):
        return ans.append(str(s_list))
    else:
        visited = [False] * 256
        for i in range(index, len(s_list)):
            if not visited[ord(s_list[i])]:
                visited[ord(s_list[i])] = True
                swap(s_list, i, index)
                g2(s_list, index + 1, ans)
                swap(s_list, i, index)


def swap(chs: list, i: int, j: int):
    tmp = chs[i]
    chs[i] = chs[j]
    chs[j] = tmp


if __name__ == '__main__':
    test = "acc"
    ans1 = permutation1(test)
    for e in ans1:
        print(e)
    print("===================")
    ans2 = permutation2(test)
    for e in ans2:
        print(e)
    print("===================")
    ans3 = permutation3(test)
    for e in ans3:
        print(e)

    # p = ""
    # print(type(p))
    # test_list = list(test)
    # for c in test_list:
    #     print(type(c))

    # a = ['a', 'b', 'c']
    # print(a)
    # a.remove('b')
    # print(a)
    # a.insert(1, 'b')
    # print(a)