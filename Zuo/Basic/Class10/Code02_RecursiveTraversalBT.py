# -*- coding: utf-8 -*-

"""
@File: Code02_RecursiveTraversalBT.py
@Author: Sarah Shen
@Time: 21/10/2022 15:30
"""


class Node:

    def __init__(self, v: int):
        self.value = v
        self.left = None
        self.right = None


def f(head):
    # 二叉树的递归序
    if head is None:
        return
    # 1
    f(head.left)
    # 2
    f(head.right)
    # 3


def pre(head):
    """ 先序打印所有节点的值 """
    if head is None:
        return
    print(head.value)
    pre(head.left)
    pre(head.right)


def inter(head):
    """ 中序打印所有节点的值 """
    if head is None:
        return
    inter(head.left)
    print(head.value)
    inter(head.right)


def pos(head):
    """ 后序打印所有节点的值 """
    if head is None:
        return
    pos(head.left)
    pos(head.right)
    print(head.value)


if __name__ == "__main__":
    h = Node(1)
    h.left = Node(2)
    h.right = Node(3)
    h.left.left = Node(4)
    h.left.right = Node(5)
    h.right.left = Node(6)
    h.right.right = Node(7)

    pre(h)
    print("========")
    inter(h)
    print("========")
    pos(h)
    print("========")
