# -*- coding: utf-8 -*-

"""
@File: Code01_MorrisTraversal.py
@Author: Sarah Shen
@Time: 08/11/2022 11:41
"""


class Node:

    def __init__(self, v: int):
        self.value = v
        self.left = None
        self.right = None


def process(root: Node):
    """ 递归序遍历 """
    if root is None:
        return
    # 这里打印是先序遍历
    process(root.left)
    # 这里打印是中序遍历
    process(root.right)
    # 这里打印是后序遍历


def morris(head):
    """
    morris遍历细节：
    假设当前节点来到cur， 开始时cur来到头节点的位置
    1. 如果cur没有左树，cur向有移动 cur = cur.right
    2. 如果cur有左树，找到左树最有的节点most_right
    1.1 如果most_right的右指针指向空，让其指向cur，然后cur向左移动 cur = cur.left
    1.2 如果most_right的有指针指向cur，让其指向空，然后cur向右移动 cur = cur.right
    3. cur为空的时候停止遍历
    """
    if head is None:
        return
    cur = head
    while cur is not None:
        most_right = cur.left
        if most_right is not None:
            while most_right.right is not None and most_right.right != cur:
                most_right = most_right.right
            if most_right.right is None:
                most_right.right = cur
                cur = cur.left
                continue
            else:
                most_right.right = None
        cur = cur.right


def morris_pre(head):
    if head is None:
        return
    cur = head
    while cur is not None:
        most_right = cur.left
        if most_right is not None:
            while most_right.right is not None and most_right.right != cur:
                most_right = most_right.right
            if most_right.right is None:
                print(str(cur.value) + " ")  # 在这里打印先序
                most_right.right = cur
                cur = cur.left
                continue
            else:
                most_right.right = None
        else:
            print(str(cur.value) + " ")
        cur = cur.right
    print()


def morris_in(head):
    if head is None:
        return
    cur = head
    while cur is not None:
        most_right = cur.left
        if most_right is not None:
            while most_right.right is not None and most_right.right != cur:
                most_right = most_right.right
            if most_right.right is None:
                most_right.right = cur
                cur = cur.left
                continue
            else:
                most_right.right = None
        print(str(cur.value), " ")  # 在这里打印中序遍历
        cur = cur.right
    print()


def morris_pos(head):
    if head is None:
        return
    cur = head
    while cur is not None:
        most_right = cur.left
        if most_right is not None:
            while most_right.right is not None and most_right.right != cur:
                most_right = most_right.right
            if most_right.right is None:
                most_right.right = cur
                cur = cur.left
                continue
            else:
                most_right.right = None
                print_edge(cur.left)
        cur = cur.right

    print_edge(head)
    print()


def print_edge(head):
    tail = reverse_edge(head)
    cur = tail
    while cur is not None:
        print(str(cur.value) + " ")
        cur = cur.right
    reverse_edge(tail)


def reverse_edge(from_node):
    pre = None
    nxt = None
    while from_node is not None:
        nxt = from_node.right
        from_node.right = pre
        pre = from_node
        from_node = nxt
    return pre


class PrintBT:

    def print_tree(self, head):
        # print("Binary Tree:")
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


if __name__ == '__main__':
    head = Node(4)
    head.left = Node(2)
    head.right = Node(6)
    head.left.left = Node(1)
    head.left.right = Node(3)
    head.right.left = Node(5)
    head.right.right = Node(7)

    pt = PrintBT()
    pt.print_tree(head)
    morris_in(head)
    morris_pre(head)
    morris_pos(head)
    pt.print_tree(head)
