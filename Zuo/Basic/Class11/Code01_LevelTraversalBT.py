# -*- coding: utf-8 -*-

"""
@File: Code01_LevelTraversalBT.py
@Author: Sarah Shen
@Time: 21/10/2022 15:50
"""

from queue import Queue


class Node:

    def __init__(self, v: int):
        self.value = v
        self.left = None
        self.right = None


def level(head):
    if head is None:
        return
    q = Queue()
    q.put(head)
    while not q.empty():
        cur = q.get()
        print(cur.value)
        if cur.left is not None:
            q.put(cur.left)
        if cur.right is not None:
            q.put(cur.right)


if __name__ == "__main__":
    h = Node(1)
    h.left = Node(2)
    h.right = Node(3)
    h.left.left = Node(4)
    h.left.right = Node(5)
    h.right.left = Node(6)
    h.right.right = Node(7)

    level(h)
    print("========")
