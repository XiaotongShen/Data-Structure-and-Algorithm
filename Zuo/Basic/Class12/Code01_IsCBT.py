# -*- coding: utf-8 -*-

"""
@File: Code01_IsCBT.py
@Author: Sarah Shen
@Time: 21/10/2022 15:51
"""
from queue import Queue


class Node:

    def __init__(self, v: int):
        self.value = v
        self.left = None
        self.right = None


def is_cbt1(head):
    if head is None:
        return True
    que = Queue()
    leaf = False

    que.put(head)
    while not que.empty():
        head = que.get()
        left = head.left
        right = head.right
        if ((leaf and (left is not None or right is not None)) or
                (left is None and right is not None)):
            return False
        if left is not None:
            que.put(left)
        if right is not None:
            que.put(right)
        if left is None or right is None:
            leaf = True
    return True


def is_cbt2(head):
    if head is None:
        return True
    return process(head).is_cbt


class Info:

    def __init__(self, f: bool, cbt: bool, h: int):
        self.is_full = f
        self.is_cbt = cbt
        self.height = h


def process(x):
    if x is None:
        return Info(True, True, 0)
    # 计算height
    left_info = process(x.left)
    right_info = process(x.right)
    height = max(left_info.height, right_info.height) + 1
    # 判断是否完全
    is_full = left_info.is_full and right_info.is_full and left_info.height == right_info.height
    is_cbt = False
    if is_full:
        is_cbt = True
    else:
        if left_info.is_cbt and right_info.is_cbt:
            if left_info.is_cbt and right_info.is_full and left_info.height == right_info.height + 1:
                is_cbt = True
            if left_info.is_full and right_info.is_full and left_info.height == right_info.height + 1:
                is_cbt = True
            if left_info.is_full and right_info.is_cbt and left_info.height == right_info.height:
                is_cbt = True
    return Info(is_full, is_cbt, height)


if __name__ == '__main__':
    hd = Node(7)
    hd.left = Node(4)
    hd.right = Node(9)
    hd.left.left = Node(1)
    hd.left.right = Node(5)

    print(is_cbt1(hd))
    print(is_cbt1(hd))

    hd1 = Node(7)
    hd1.left = Node(4)
    hd1.right = Node(9)
    hd1.left.left = Node(1)
    hd1.left.right = Node(5)
    hd1.left.left.left = Node(8)
    hd1.left.right.right = Node(10)

    print(is_cbt1(hd1))
    print(is_cbt1(hd1))
