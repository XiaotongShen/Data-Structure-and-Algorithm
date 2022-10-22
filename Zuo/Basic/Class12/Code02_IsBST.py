# -*- coding: utf-8 -*-

"""
@File: Code02_IsBST.py
@Author: Sarah Shen
@Time: 21/10/2022 15:51
"""

class Node:

    def __init__(self, v: int):
        self.value = v
        self.left = None
        self.right = None


def is_bst1(head):
    if head is None:
        return True
    arr = list()
    inner(head, arr)
    for i in range(1, len(arr)):
        if arr[i].value <= arr[i - 1].value:
            return False
    return True


def inner(head, arr):
    if head is None:
        return
    inner(head.left, arr)
    arr.append(head)
    inner(head.right, arr)


def is_bst2(head):
    if head is None:
        return True
    return process(head).is_bst


class Info:

    def __init__(self, i: bool, max_v: int, min_v: int):
        self.is_bst = i
        self.max = max_v
        self.min = min_v


def process(x):
    if x is None:
        return None
    left_info = process(x.left)
    right_info = process(x.right)
    # 获得最大值，最小值
    max_value = x.value
    if left_info is not None:
        max_value = max(max_value, left_info.max)
    if right_info is not None:
        max_value = max(max_value, right_info.max)
    min_value = x.value
    if left_info is not None:
        min_value = min(min_value, left_info.min)
    if right_info is not None:
        min_value = min(min_value, right_info.min)
    # 判断是否是搜索二叉树
    is_bst = True
    if left_info is not None and not left_info.is_bst:
        is_bst = False
    if right_info is not None and not right_info.is_bst:
        is_bst = False
    if left_info is not None and left_info.max >= x.value:
        is_bst = False
    if right_info is not None and right_info.min <= x.value:
        is_bst = False
    return Info(is_bst, max_value, min_value)


if __name__ == '__main__':
    h = Node(7)
    h.left = Node(4)
    h.right = Node(9)
    h.left.left = Node(1)
    h.left.right = Node(5)
    h.right.left = Node(8)
    h.right.right = Node(10)

    print(is_bst1(h))
    print(is_bst2(h))
