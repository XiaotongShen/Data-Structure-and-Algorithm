# -*- coding: utf-8 -*-

"""
@File: Code01_IsCBT.py
@Author: Sarah Shen
@Time: 23/10/2022 00:23
"""
from queue import Queue
# 测试链接 : https://leetcode.com/problems/check-completeness-of-a-binary-tree/


class TreeNode:

    def __init__(self, v: int):
        self.value = v
        self.right = None
        self.left = None


def is_complete_tree1(head):
    if head is None:
        return True
    que = Queue()
    leaf = False
    l = None
    r = None
    que.put(head)
    while not que.empty():
        head = que.get()
        l = head.left
        r = head.right
        if leaf and (l is not None or r is not None) or (l is None and r is not None):
            return False
        if l is not None:
            que.put(l)
        if r is not None:
            que.put(r)
        if l is None or r is None:
            leaf = True
    return True


def is_complete_tree2(head):
    return process(head).is_cbt


class Info:

    def __init__(self, f: bool, cbt: bool, h: int):
        self.is_full = f
        self.is_cbt = cbt
        self.height = h


def process(x):
    if x is None:
        return Info(True, True, 0)
    left_info = process(x.left)
    right_info = process(x.right)
    # 高度计算
    height = max(left_info.height, right_info.height) + 1
    is_full = left_info.is_full and right_info.is_full and left_info.height == right_info.height
    is_cbt = False
    # 情况1：左树满，右树满，且左右高度一致
    if left_info.is_full and right_info.is_full and left_info.height == right_info.height:
        is_cbt = True
    # 情况2：左树完全，右树满，且左树高度比右树高度大1
    if left_info.is_cbt and right_info.is_full and left_info.height == right_info.height + 1:
        is_cbt = True
    # 情况3：左树满，右树满，且左树高度比右树高度大1
    if left_info.is_full and right_info.is_full and left_info.height == right_info.height + 1:
        is_cbt = True
    # 情况4：左树满，右树完全，且左树高度等于右树高度
    if left_info.is_full and right_info.is_cbt and left_info.height == right_info.height:
        is_cbt = True
    return Info(is_full, is_cbt, height)


if __name__ == '__main__':
    h0 = TreeNode(1)
    h0.left = TreeNode(2)
    h0.right = TreeNode(3)
    h0.left.left = TreeNode(4)
    h0.right.left = TreeNode(6)

    h1 = TreeNode(1)
    h1.left = TreeNode(2)
    h1.right = TreeNode(3)

    h2 = TreeNode(1)
    h2.left = TreeNode(2)
    h2.right = TreeNode(3)
    h2.left.left = TreeNode(4)

    h3 = TreeNode(1)
    h3.left = TreeNode(2)
    h3.right = TreeNode(3)
    h3.left.left = TreeNode(4)
    h3.left.right = TreeNode(5)

    h4 = TreeNode(1)
    h4.left = TreeNode(2)
    h4.right = TreeNode(3)
    h4.left.left = TreeNode(4)
    h4.left.right = TreeNode(5)
    h4.right.left = TreeNode(6)

    print(is_complete_tree2(h0))
    print(is_complete_tree2(h1))
    print(is_complete_tree2(h2))
    print(is_complete_tree2(h3))
    print(is_complete_tree2(h4))
    print()
    print(is_complete_tree1(h0))
    print(is_complete_tree1(h1))
    print(is_complete_tree1(h2))
    print(is_complete_tree1(h3))
    print(is_complete_tree1(h4))
