# -*- coding: utf-8 -*-

"""
@File: Code06_SuccessorNode.py
@Author: Sarah Shen
@Time: 21/10/2022 15:50
"""


# TODO: 11-06待完成
class Node:

    def __init__(self, v: int):
        self.value = v
        self.left = None
        self.right = None
        self.parent = None


def get_successor_node(node):
    if node is None:
        return node
    if node.right is not None:
        # 有右树，获取右树最左的节点
        return get_left_most(node)
    else:
        # 没有右树
        p = node.parent
        while p is not None and p.right == node:
            # 当前节点node是其parent的右树
            node = p  # 当前节点向上移动
            p = node.parent  # 上一个节点的父节点
        return p


def get_left_most(node):
    if node is None:
        return node
    while node.left is not None:
        node = node.left
    return node


if __name__ == "__main__":
    head = Node(6)
    head.left = Node(10)
    head.left.parent = head
    head.left.left = Node(1)
    head.left.left.parent = head.left
    head.left.left.right = Node(2)
    head.left.left.right.parent = head.left.left
    head.left.right = Node(4)
    head.left.right.parent = head.left
    head.left.right.right = Node(5)
    head.left.right.right.parent = head.left.right
    head.right = Node(9)
    head.right.parent = head
    head.right.left = Node(8)
    head.right.left.parent = head.right
    head.right.left.left = Node(8)
    head.right.left.left.parent = head.right.left
    head.right.right = Node(10)
    head.right.right.parent = head.right

    test = head.left.left
    print(str(test.value) + " next: " + str(get_successor_node(test).value))
    test = head.left.left.right
    print(str(test.value) + " next: " + str(get_successor_node(test).value))
    test = head.left
    print(str(test.value) + " next: " + str(get_successor_node(test).value))
    test = head.left.right
    print(str(test.value) + " next: " + str(get_successor_node(test).value))
    test = head.left.right.right
    print(str(test.value) + " next: " + str(get_successor_node(test).value))
    test = head
    print(str(test.value) + " next: " + str(get_successor_node(test).value))
    test = head.right.left.left
    print(str(test.value) + " next: " + str(get_successor_node(test).value))
    test = head.right.left
    print(str(test.value) + " next: " + str(get_successor_node(test).value))
    test = head.right
    print(str(test.value) + " next: " + str(get_successor_node(test).value))
    test = head.right.right  # 10's next is null
    print(str(test.value) + " next: " + str(get_successor_node(test)))
