# -*- coding: utf-8 -*-

"""
@File: Code06_MaxDistance.py
@Author: Sarah Shen
@Time: 21/10/2022 15:51
"""


class Node:

    def __init__(self, v: int):
        self.value = v
        self.left = None
        self.right = None


def max_distance1(head):
    if head is None:
        return 0
    arr = get_pre_list(head)
    parent_map = get_parent_map(head)
    max_distance = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            max_distance = max(max_distance, distance(parent_map, arr[i], arr[j]))
    return max_distance


def get_pre_list(head):
    arr = list()
    fill_pre_list(head, arr)
    return arr


def fill_pre_list(head, arr):
    if head is None:
        return
    arr.append(head)
    fill_pre_list(head.left, arr)
    fill_pre_list(head.right, arr)


def get_parent_map(head):
    p_map = dict()
    p_map[head] = None
    fill_parent_map(head, p_map)
    return p_map


def fill_parent_map(head, parent_map):
    if head.left is not None:
        parent_map[head.left] = head
        fill_parent_map(head.left, parent_map)
    if head.right is not None:
        parent_map[head.right] = head
        fill_parent_map(head.right, parent_map)


def distance(parent_map, o1, o2):
    o1_set = dict()
    cur = o1
    o1_set[cur] = True
    while parent_map.get(cur) is not None:
        cur = parent_map.get(cur)
        o1_set[cur] = True
    cur = o2
    while not o1_set.keys().__contains__(cur):
        cur = parent_map.get(cur)
    lowest_ancestor = cur
    cur = o1
    distance1 = 1
    while cur != lowest_ancestor:
        cur = parent_map.get(cur)
        distance1 += 1
    cur = o2
    distance2 = 1
    while cur != lowest_ancestor:
        cur = parent_map.get(cur)
        distance2 += 1
    return distance1 + distance2 - 1


if __name__ == '__main__':
    hd1 = Node(7)
    hd1.left = Node(4)
    hd1.right = Node(9)
    hd1.left.left = Node(1)
    hd1.left.right = Node(5)
    hd1.left.left.left = Node(8)
    hd1.left.right.right = Node(10)
    hd1.left.right.right.right = Node(12)
    hd1.left.right.right.right.right = Node(14)
    hd1.left.right.right.right.right.right = Node(15)

    hd2 = Node(7)
    hd2.left = Node(4)
    hd2.right = Node(9)
    hd2.left.left = Node(1)
    hd2.left.right = Node(5)
    hd2.right.left = Node(8)
    hd2.right.right = Node(10)

    print(max_distance1(hd1))
    print(max_distance1(hd2))
