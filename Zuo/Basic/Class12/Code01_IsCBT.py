# -*- coding: utf-8 -*-

"""
@File: Code01_IsCBT.py
@Author: Sarah Shen
@Time: 21/10/2022 15:51
"""


class Node:

    def __init__(self, v: int):
        self.value = v
        self.left = None
        self.right = None


def is_balanced1(head):
    ans = [None]
    ans[0] = True
    process1(head, ans)
    return ans[0]


def process1(head, ans: list):
    if not ans[0] or head is None:
        return -1
    left_height = process1(head.left, ans)
    right_height = process1(head.right, ans)
    if abs(left_height - right_height) > 1:
        ans[0] = False
    return max(left_height, right_height) + 1


def is_balanced2(head):
    return process(head).is_balanced


class Info:

    def __init__(self, i: bool, h: int):
        self.is_balanced = i
        self.height = h


def process(x):
    if x is None:
        return Info(True, 0)
    # 计算height
    left_info = process(x.left)
    right_info = process(x.right)
    height = max(left_info.height, right_info.height) + 1
    # 判断是否平衡
    is_balanced = True
    if not left_info.is_balanced:
        is_balanced = False
    if not right_info.is_balanced:
        is_balanced = False
    if abs(left_info.height - right_info.height) > 1:
        is_balanced = False
    return Info(is_balanced, height)


if __name__ == '__main__':
    hd = Node(7)
    hd.left = Node(4)
    hd.right = Node(9)
    hd.left.left = Node(1)
    hd.left.right = Node(5)

    print(is_balanced1(hd))
    print(is_balanced2(hd))

    hd1 = Node(7)
    hd1.left = Node(4)
    hd1.right = Node(9)
    hd1.left.left = Node(1)
    hd1.left.right = Node(5)
    hd1.left.left.left = Node(8)
    hd1.left.right.right = Node(10)

    print(is_balanced1(hd1))
    print(is_balanced2(hd1))
