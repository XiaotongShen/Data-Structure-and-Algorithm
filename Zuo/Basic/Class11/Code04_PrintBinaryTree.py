# -*- coding: utf-8 -*-

"""
@File: Code04_PrintBinaryTree.py
@Author: Sarah Shen
@Time: 21/10/2022 15:50
"""
import sys


class Node:

    def __init__(self, v: int):
        self.value = v
        self.left = None
        self.right = None


class PrintBT:

    def print_tree(self, head):
        print("Binary Tree:")
        self.print_in_order(head, 0, "H", 17)
        print()

    def print_in_order(self, head, height: int, to: str, length: int):
        if head is None:
            return
        self.print_in_order(head.right, height + 1, "v", length)
        val = to + str(head.value) + to
        len_m = len(val)
        len_l = int((length - len_m) / 2)
        len_r = length - len_m - len_l
        val = self.get_space(len_l) + val + self.get_space(len_r)
        print(self.get_space(height * length) + val)
        self.print_in_order(head.left, height + 1, "^", length)

    @staticmethod
    def get_space(num: int):
        space = " "
        buf = ""
        for i in range(num):
            buf += space
        return buf


if __name__ == "__main__":
    pbt = PrintBT()

    h1 = Node(1)
    h1.left = Node(-222222222)
    h1.right = Node(3)
    h1.left.left = Node(-sys.maxsize - 1)
    h1.right.left = Node(55555555)
    h1.right.right = Node(66)
    h1.left.left.right = Node(777)
    pbt.print_tree(h1)

    h2 = Node(1)
    h2.left = Node(2)
    h2.right = Node(3)
    h2.left.left = Node(4)
    h2.right.left = Node(5)
    h2.right.right = Node(6)
    h2.left.left.right = Node(7)
    pbt.print_tree(h2)

    h3 = Node(1)
    h3.left = Node(1)
    h3.right = Node(1)
    h3.left.left = Node(1)
    h3.right.left = Node(1)
    h3.right.right = Node(1)
    h3.left.left.right = Node(1)
    pbt.print_tree(h3)

    a = "12345"
    print(len(a))
