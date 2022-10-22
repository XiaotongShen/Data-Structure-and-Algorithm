# -*- coding: utf-8 -*-

"""
@File: Code04_isFull.py
@Author: Sarah Shen
@Time: 21/10/2022 15:51
"""


# TODO：12-04 待完成


class Node:

    def __init__(self, v: int):
        self.value = v
        self.left = None
        self.right = None


# 第一种方法：收集整颗树的高度和节点数
# 满足如下条件的是满二叉树： 2^h - 1 == n
def is_full1(head):
    if head is None:
        return True
    node_info = process1(head)
    return (1 << node_info.height) - 1 == node_info.nodes


class Info1:

    def __init__(self, h: int, n: int):
        self.height = h
        self.nodes = n


def process1(head):
    if head is None:
        return Info1(0, 0)
    left_info = process1(head.left)
    right_info = process1(head.right)
    height = max(left_info.height, right_info.height) + 1
    nodes = left_info.nodes + right_info.nodes + 1
    return Info1(height, nodes)


"""
第二种方法： 
收集子树是否是满二叉树
收集子树的高度
左树满 and 右树慢 and 左右树高度一样 -> 整棵树是满的
"""


def is_full2(head):
    if head is None:
        return True
    return process2(head).is_full


class Info2:

    def __init__(self, f: bool, h: int):
        self.is_full = f
        self.height = h


def process2(head):
    if head is None:
        return Info2(True, 0)
    left_info = process2(head.left)
    right_info = process2(head.right)
    is_full = left_info.is_full and right_info.is_full and left_info.height == right_info.height
    height = max(left_info.height, right_info.height) + 1
    return Info2(is_full, height)


if __name__ == '__main__':
    hd1 = Node(7)
    hd1.left = Node(4)
    hd1.right = Node(9)
    hd1.left.left = Node(1)
    hd1.left.right = Node(5)
    hd1.left.left.left = Node(8)
    hd1.left.right.right = Node(10)

    print(is_full1(hd1))
    print(is_full2(hd1))
    print()

    hd2 = Node(7)
    hd2.left = Node(4)
    hd2.right = Node(9)
    hd2.left.left = Node(1)
    hd2.left.right = Node(5)
    hd2.right.left = Node(8)
    hd2.right.right = Node(10)
    print(is_full1(hd2))
    print(is_full2(hd2))
