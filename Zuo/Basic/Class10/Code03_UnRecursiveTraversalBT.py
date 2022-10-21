# -*- coding: utf-8 -*-

"""
@File: Code03_UnRecursiveTraversalBT.py
@Author: Sarah Shen
@Time: 21/10/2022 15:30
"""


class Node:

    def __init__(self, v: int):
        self.value = v
        self.left = None
        self.right = None


def pre(head):
    """ 用栈容器实现先序遍历 """
    print("pre-order: ")
    if head is not None:
        stack = list()
        stack.append(head)
        while len(stack) != 0:
            # 如果栈不为空，弹出第一个节点就打印
            head = stack.pop()
            print(str(head.value) + " ")
            # 检查当前节点的右树和左树，依次压入栈，注意（先右后左）
            if head.right is not None:
                stack.append(head.right)
            if head.left is not None:
                stack.append(head.left)
    print()


def inter(head):
    print("in-order: ")
    if head is not None:
        s = list()
        while len(s) != 0 or head is not None:
            if head is not None:
                s.append(head)
                head = head.left  # 如果左树不为空，就加入
            else:
                head = s.pop()
                print(str(head.value) + " ")
                head = head.right
    print()


def pos1(head):
    print("pos-order1: ")
    if head is not None:
        s1 = list()
        s2 = list()
        s1.append(head)
        while len(s1) != 0:
            head = s1.pop()  # 头 右 左
            s2.append(head)
            if head.left is not None:
                s1.append(head.left)
            if head.right is not None:
                s1.append(head.right)
        while len(s2) != 0:
            print(str(s2.pop().value) + " ")
    print()


def pos2(head):
    print("pos-order2: ")
    if head is not None:
        s = list()
        s.append(head)
        while len(s) != 0:
            cur = s[len(s)-1]  # 弹出的node
            if cur.left is not None and head != cur.left and head != cur.right:
                s.append(cur.left)
            elif cur.right is not None and head != cur.right:
                s.append(cur.right)
            else:
                print(str(s.pop().value) + " ")
                head = cur
    print()


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
    pos1(h)
    print("========")
    pos2(h)
    print("========")
