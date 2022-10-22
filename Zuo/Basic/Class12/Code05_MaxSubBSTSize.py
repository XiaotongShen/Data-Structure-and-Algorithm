# -*- coding: utf-8 -*-

"""
@File: Code05_MaxSubBSTSize.py
@Author: Sarah Shen
@Time: 21/10/2022 15:51
"""


# 在线测试链接 : https://leetcode.com/problems/largest-bst-subtree


class TreeNode:

    def __init__(self, v: int):
        self.value = v
        self.left = None
        self.right = None


def largest_bst_subtree(head):
    if head is None:
        return 0
    return process(head).max_bst_subtree_size


class Info:

    def __init__(self, s: int, a: int, max_v: int, min_v: int):
        self.max_bst_subtree_size = s
        self.all_size = a
        self.max = max_v
        self.min = min_v


def process(x):
    if x is None:
        return None
    left_info = process(x.left)
    right_info = process(x.right)
    max_val = x.value
    min_val = x.value
    all_size = 1
    if left_info is not None:
        max_val = max(left_info.max, max_val)
        min_val = min(left_info.min, min_val)
        all_size += left_info.all_size
    if right_info is not None:
        max_val = max(right_info.max, max_val)
        min_val = min(right_info.min, min_val)
        all_size += right_info.all_size
    # 接下来分情况讨论
    p1 = -1
    if left_info is not None:
        p1 = left_info.max_bst_subtree_size
    p2 = -1
    if right_info is not None:
        p2 = right_info.max_bst_subtree_size
    p3 = -1
    left_bst = True if left_info is None else left_info.max_bst_subtree_size == left_info.all_size
    right_bst = True if right_info is None else right_info.max_bst_subtree_size == right_info.all_size
    if left_bst and right_bst:
        left_max_less_x = True if left_info is None else left_info.max < x.value
        right_min_more_x = True if right_info is None else right_info.min > x.value
        if left_max_less_x and right_min_more_x:
            left_size = 0 if left_info is None else left_info.all_size
            right_size = 0 if right_info is None else right_info.all_size
            p2 = left_size + right_size + 1
    return Info(max(p1, max(p2, p3)), all_size, max_val, min_val)
