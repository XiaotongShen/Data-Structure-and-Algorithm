# -*- coding: utf-8 -*-

"""
@File: Code04_MaxHappy.py
@Author: Sarah Shen
@Time: 23/10/2022 00:24
"""


# TODO


class Node:

    def __init__(self, v: int):
        self.value = v
        self.children = list()


def max_happy1(head):
    if head is None:
        return 0
    return process1(head, False)


def process1(cur, up):
    if up:
        # 如果cur的上级来的话，cur没的选，只能不来
        ans = 0
        for child in cur.children:
            ans += process1(child, False)
        return ans
    else:
        p1 = cur.value
        p2 = 0
        for child in cur.children:
            p1 += process1(child, True)
            p2 += process1(child, False)
        return max(p1, p2)


# 方法2：二叉树遍历递归套路
# 1. 可以选节点，发party邀请
# 2. 直接上下级不要一起请
# 3. 选完节点后，所有被邀请的人快乐值最大

# 转化为在x为头的时候，最大的happy值是什么
# 情况1：在x来的时候最大的happy值是多少
#   x自己的快乐值 + 其children都不来的情况下最大的happy值
# 情况2：在x不来的时候最大的happy值是多少
#   x自己的快乐值0 + 其children所有情况（来或不来）下的最大happy值


def max_happy2(head):
    all_info = process(head)
    return max(all_info.yes, all_info.no)


class Info:

    def __init__(self, n: int, y: int):
        self.no = n
        self.yes = y


def process(x):
    if x is None:
        return Info(0, 0)
    no = 0
    yes = x.value
    for child in x.children:
        next_info = process(child)
        no += max(next_info.no, next_info.yes)
        yes += next_info.no
    return Info(no, yes)
