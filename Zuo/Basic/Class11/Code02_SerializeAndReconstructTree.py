# -*- coding: utf-8 -*-

"""
@File: Code02_SerializeAndReconstructTree.py
@Author: Sarah Shen
@Time: 21/10/2022 15:50
"""
from queue import Queue

# TODO: 11-02待完成
"""
#二叉树可以通过先序，后序或者按层遍历的方式序列化和反序列化
以下代码全部实现了
但是，二叉树无法通过中序遍历的方式实现序列化和反序列化
因为不同的两颗树，可能得到同样的中序序列，即使补充了空位置也可能一样
比如以下两棵树
        __2
      /
      1
      和
      1__
         \
         2
补足空位置的中序遍历结果都是 null, 1, null, 2, null
"""


class Node:

    def __init__(self, v: int):
        self.value = v
        self.left = None
        self.right = None


def pre_serial(head):
    ans = Queue()
    pres(head, ans)
    return ans


def pres(head, ans):
    if head is None:
        ans.put(None)
    else:
        ans.put(str(head.value))
        pres(head.left, ans)
        pres(head.right, ans)


def ins_serial(head):
    ans = Queue()
    ins(head, ans)
    return ans


def ins(head, ans):
    if head is None:
        ans.put(None)
    else:
        ins(head.left, ans)
        ans.put(str(head.value))
        ins(head.right, ans)


def pos_serial(head):
    ans = Queue()
    poss(head, ans)
    return ans


def poss(head, ans):
    if head is None:
        ans.put(None)
    else:
        poss(head.left, ans)
        poss(head.right, ans)
        ans.put(str(head.value))


def build_by_pre_queue(pre_list):
    if pre_list is None or pre_list.qsize == 0:
        return None
    return pre_b(pre_list)


def pre_b(pre_list):
    cur = pre_list.get()
    if cur is None:
        return None
    head = Node(int(cur))
    head.left = pre_b(pre_list)
    head.right = pre_b(pre_list)
    return head


def build_by_pos_queue(pos_list):
    if pos_list is None or pos_list.qsize == 0:
        return None
        # 左右中 -> stack 中左右
    s = list()
    while not pos_list.empty():
        s.append(pos_list.get())
    return pos_b(s)


def pos_b(pos_stack):
    cur = pos_stack.pop()
    if cur is None:
        return None
    head = Node(int(cur))
    head.right = pos_b(pos_stack)
    head.left = pos_b(pos_stack)
    return head


def level_serial(head):
    ans = Queue()
    if head is None:
        ans.put(None)
    else:
        ans.put(str(head.value))
        q = Queue()
        q.put(head)
        while not q.empty():
            head = q.get()
            if head.left is not None:
                ans.put(str(head.left.value))
                q.put(head.left)
            else:
                ans.put(None)
            if head.right is not None:
                ans.put(str(head.right.value))
                q.put(head.right)
            else:
                ans.put(None)
    return ans


def build_by_level_queue(level_list):
    if level_list is None or level_list.qsize() == 0:
        return None
    head = generate_node(level_list.get())
    q = Queue()
    if head is not None:
        q.put(head)
    while not q.empty():
        node = q.get()
        node.left = generate_node(level_list.get())
        node.right = generate_node(level_list.get())
        if node.left is not None:
            q.put(node.left)
        if node.right is not None:
            q.put(node.right)
    return head


def generate_node(val):
    if val is None:
        return None
    return Node(int(val))


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
    h2 = Node(1)
    h2.left = Node(2)
    h2.right = Node(3)
    h2.left.left = Node(4)
    h2.right.left = Node(5)
    h2.right.right = Node(6)
    h2.left.left.right = Node(7)

    pre_l = pre_serial(h2)
    ins_l = ins_serial(h2)
    pos_l = pos_serial(h2)
    lvl_l = level_serial(h2)

    pre_h = build_by_pre_queue(pre_l)
    pos_h = build_by_pos_queue(pos_l)
    lvl_h = build_by_level_queue(lvl_l)

    btp = PrintBT()
    print("Original")
    btp.print_tree(h2)
    print("Build by Pre")
    btp.print_tree(pre_h)
    print("Build by Pos")
    btp.print_tree(pos_h)
    print("Build by Level")
    btp.print_tree(lvl_h)
