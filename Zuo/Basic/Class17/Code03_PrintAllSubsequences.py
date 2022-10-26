# -*- coding: utf-8 -*-

"""
@File: Code03_PrintAllSubsequences.py
@Author: Sarah Shen
@Time: 26/10/2022 10:04
"""


# 打印字符串所有子序列
def subs(s: str):
    str_list = list(s)
    path = ""
    ans = list()
    process1(str_list, 0, ans, path)
    return ans


def process1(s: list, index: int, ans: list, path: str):
    if index == len(s):
        ans.append(path)
        return
        # 没有要index位置的字符，path不变，继续看下一个位置
    process1(s, index + 1, ans, path)
    # 要了index位置的字符，path加index位置的字符，继续看下一个位置
    process1(s, index + 1, ans, path + str(s[index]))


# 打印不重复的字符串子序列
def subs_no_repeat(s: str):
    str_list = list(s)
    path = ""
    ans_set = set()
    process2(str_list, 0, ans_set, path)
    ans = list()
    for cur in ans_set:
        ans.append(cur)
    return ans


def process2(s: list, index: int, ans_set: set, path: str):
    if index == len(s):
        ans_set.add(path)
        return
    no = path
    process2(s, index + 1, ans_set, no)
    yes = path + str(s[index])
    process2(s, index + 1, ans_set, yes)


if __name__ == '__main__':
    test = "acccc"
    ans1 = subs(test)
    ans2 = subs_no_repeat(test)
    for e in ans1:
        print(e)
    print("====================")
    for e in ans2:
        print(e)
    print("====================")
