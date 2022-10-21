# -*- coding: utf-8 -*-

"""
@File: Code03_EncodeNaryTreeToBinaryTree.py
@Author: Sarah Shen
@Time: 21/10/2022 15:50
"""


class Node:

    def __init__(self, v: int, c: list):
        self.value = v
        self.children = c


class TreeNode:

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


class Codec:

    def encode(self, root):
        """ Encodes an n-ary tree to ba binary tree """
        if root is None:
            return None
        head = TreeNode(root.value)
        head.left = self.en(root.children)
        return head

    def en(self, children):
        head = None
        cur = None
        for child in children:
            t_node = TreeNode(child.value)
            if head is None:
                head = t_node
            else:
                cur.right = t_node
            cur = t_node
            cur.left = self.en(child.children)
        return head

    def decode(self, root):
        if root is None:
            return None
        return Node(root.value, self.de(root.left))

    def de(self, root):
        children = list()
        while root is not None:
            cur = Node(root.value, self.de(root.left))
            children.append(cur)
            root = root.right
        return children


if __name__ == "__main__":
    r1 = Node(1, [
        Node(2, [Node(5, list()), Node(6, list()), Node(7, list()), Node(8, list())]),
        Node(3, [Node(9, list()), Node(10, list()), Node(11, list())]),
        Node(4, [Node(12, list())])
    ])

    pbt = PrintBT()
    cc = Codec()

    h = cc.encode(r1)
    pbt.print_tree(h)

    r2 = cc.decode(h)
    h1 = cc.encode(r2)
    pbt.print_tree(h1)
