# -*- coding: utf-8 -*-

"""
@File: Code02_MaxSubBSTHead.py
@Author: Sarah Shen
@Time: 23/10/2022 00:23
"""


class Node:

    def __init__(self, v: int):
        self.value = v
        self.left = None
        self.right = None


# 方法1
def get_bst_size(head):
    if head is None:
        return 0
    arr = list()
    inner(head, arr)
    for i in range(1, len(arr)):
        if arr[i].value <= arr[i - 1].value:
            return 0
    return len(arr)


def inner(head, arr):
    if head is None:
        return
    inner(head.left, arr)
    arr.append(head)
    inner(head.right, arr)


def max_sub_bst_head1(head):
    if head is None:
        return None
    if get_bst_size(head) != 0:
        return head
    left_ans = max_sub_bst_head1(head.left)
    right_ans = max_sub_bst_head1(head.right)
    return left_ans if get_bst_size(left_ans) > get_bst_size(right_ans) else right_ans


# 方法2
def max_sub_bst_head2(head):
    if head is None:
        return None
    return process(head).max_sub_bst_head


class Info:

    def __init__(self, h, s: int, min_v: int, max_v: int):
        self.max_sub_bst_head = h
        self.max_sub_bst_size = s
        self.min_value = min_v
        self.max_value = max_v


def process(x):
    if x is None:
        return None
    left_info = process(x.left)
    right_info = process(x.right)
    min_value = x.value
    max_value = x.value
    max_sub_bst_head = None
    max_sub_bst_size = 0
    if left_info is not None:
        min_value = min(min_value, left_info.min_value)
        max_value = max(max_value, right_info.max_value)
        max_sub_bst_head = left_info.max_sub_bst_head
        max_sub_bst_size = left_info.max_sub_bst_size
    if right_info is not None:
        min_value = min(min_value, right_info.min_value)
        max_value = max(max_value, right_info.max_value)
        if right_info.max_sub_bst_size > max_sub_bst_size:
            max_sub_bst_head = right_info.max_sub_bst_head
            max_sub_bst_size = right_info.max_sub_bst_size
    if (True if left_info is None else (left_info.max_sub_bst_head == x.left and left_info.max_value < x.value)) and (True if right_info is None else (right_info.max_sub_bst_head == x.right and right_info.min_value > x.value)):
        max_sub_bst_head = x
        max_sub_bst_size = (0 if left_info is None else left_info.max_sub_bst_size) + \
                           (0 if right_info is None else right_info.max_sub_bst_size) + 1
    return Info(max_sub_bst_head, max_sub_bst_size, max_value, min_value)
