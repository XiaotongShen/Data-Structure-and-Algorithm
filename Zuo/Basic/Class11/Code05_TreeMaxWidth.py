# -*- coding: utf-8 -*-

"""
@File: Code05_TreeMaxWidth.py
@Author: Sarah Shen
@Time: 21/10/2022 15:50
"""
import sys
from queue import Queue


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


def max_width_use_map(head):
    if head is None:
        return 0
    q = Queue()
    q.put(head)
    # key(level) value
    level_map = dict()
    level_map[head] = 1
    cur_level = 1  # 当前层
    cur_level_nodes = 0  # 当前层目前统计的宽度
    max_width = 0
    while not q.empty():
        cur = q.get()
        cur_node_level = level_map.get(cur)
        if cur.left is not None:
            level_map[cur.left] = cur_node_level + 1
            q.put(cur.left)
        if cur.right is not None:
            level_map[cur.right] = cur_node_level + 1
            q.put(cur.right)
        if cur_node_level == cur_level:
            cur_level_nodes += 1
        else:
            max_width = max(max_width, cur_level_nodes)
            cur_level += 1
            cur_level_nodes = 1
    max_width = max(max_width, cur_level_nodes)
    return max_width


def max_width_no_map(head):
    if head is None:
        return 0
    q = Queue()
    q.put(head)
    cur_end = head  # 当前层，最右的节点是谁
    next_end = None  # 下一层，最右的节点是谁
    max_width = 0  # 统计过的最大单层节点数
    cur_level_nodes = 0  # 当前层统计到的节点个数
    while not q.empty():
        cur = q.get()  # 从队列里取出一个节点
        if cur.left is not None:
            q.put(cur.left)  # 将当前节点存在的左树放入队列
            next_end = cur.left  # 下一层最后一个节点更新为观察到的左树
        if cur.right is not None:
            q.put(cur.right)  # 将当前节点的存在的右树放入队列
            next_end = cur.right  # 更新下一层最后一个节点
        cur_level_nodes += 1
        if cur == cur_end:
            # 到达当前层最后一个节点
            max_width = max(max_width, cur_level_nodes)
            cur_level_nodes = 0
            cur_end = next_end
    return max_width


if __name__ == "__main__":
    pbt = PrintBT()

    h1 = Node(1)
    h1.left = Node(-222222222)
    h1.right = Node(3)
    h1.left.left = Node(-sys.maxsize - 1)
    h1.right.left = Node(55555555)
    h1.right.right = Node(66)
    h1.left.left.right = Node(777)
    # pbt.print_tree(h1)
    print(max_width_use_map(h1))
    print(max_width_no_map(h1))
    print()

    h2 = Node(1)
    h2.left = Node(2)
    h2.right = Node(3)
    h2.left.left = Node(4)
    h2.right.left = Node(5)
    h2.right.right = Node(6)
    h2.left.left.right = Node(7)
    # pbt.print_tree(h2)
    print(max_width_use_map(h2))
    print(max_width_no_map(h2))
    print()

    h3 = Node(1)
    h3.left = Node(1)
    h3.right = Node(1)
    h3.left.left = Node(1)
    h3.right.left = Node(1)
    h3.right.right = Node(1)
    h3.left.left.right = Node(1)
    # pbt.print_tree(h3)
    print(max_width_use_map(h3))
    print(max_width_no_map(h3))
    print()

    # a = "12345"
    # print(len(a))
    #
    # d = dict()
