# -*- coding: utf-8 -*-

"""
@File: Code03_LowestAncestor.py
@Author: Sarah Shen
@Time: 23/10/2022 00:24
"""


# TODO
class Node:

    def __init__(self, v: int):
        self.value = v
        self.right = None
        self.left = None


# 方法1: 容器
def lowest_ancestor1(head, o1, o2):
    if head is None:
        return None
    # key的父节点是value
    parent_map = dict()
    parent_map[head] = None
    fill_parent_map(head, parent_map)
    o1_set = dict()
    cur = o1
    o1_set[cur] = True
    while parent_map.get(cur) is not None:
        cur = parent_map.get(cur)
        o1_set[cur] = True
    cur = o2
    while not o1_set.keys().__contains__(cur):
        cur = parent_map.get(cur)
    return cur


def fill_parent_map(head, parent_map):
    if head.left is not None:
        parent_map[head.left] = head
        fill_parent_map(head.left, parent_map)
    if head.right is not None:
        parent_map[head.right] = head
        fill_parent_map(head.right, parent_map)


# 方法2：二叉树遍历递归套路
# 以X开头的子树是否发现节点a和b
# info：contains a, contains b, contains mutual ancestor
# 情况1：X不是最低的汇聚点， 左树是有答案
# 情况2：X不是最低的汇聚点， 右树是有答案
# 情况3：a,b不全

# 情况4：x是汇聚点
# 情况5：x是a, 子树发现b
# 情况6：x是b，子树发现a
def lowest_ancestor2(head, a, b):
    return process(head, a, b).ans


class Info:

    def __init__(self, a: bool, b: bool, ans):
        self.find_a = a
        self.find_b = b
        self.ans = ans


def process(x, a, b):
    if x is None:
        return Info(False, False, None)
    left_info = process(x.left, a, b)
    right_info = process(x.right, a, b)
    find_a = (x == a) or left_info.find_a or right_info.find_a
    find_b = (x == b) or left_info.find_b or right_info.find_b
    ans = None
    if left_info.ans is not None:
        ans = left_info.ans
    elif right_info.ans is not None:
        ans = right_info.ans
    else:
        if find_a and find_b:
            ans = x
    return Info(find_a, find_b, ans)


if __name__ == '__main__':
    h4 = Node(1)
    h4.left = Node(2)
    h4.right = Node(3)
    h4.left.left = Node(4)
    h4.left.right = Node(5)
    h4.right.left = Node(6)
    h4.right.right = Node(7)

    n4 = h4.left.left
    n2 = h4.left  # 2
    n5 = h4.left.right  # 2
    n1 = h4  # 1
    n3 = h4.right  # 1
    n6 = h4.right.left  # 1
    n7 = h4.right.right  # 1

    print(lowest_ancestor2(h4, n4, n2).value)
    print(lowest_ancestor2(h4, n4, n5).value)
    print(lowest_ancestor2(h4, n4, n1).value)
    print(lowest_ancestor2(h4, n4, n3).value)
    print(lowest_ancestor2(h4, n4, n6).value)
    print(lowest_ancestor2(h4, n4, n7).value)
    print()

    print(lowest_ancestor1(h4, n4, n2).value)
    print(lowest_ancestor1(h4, n4, n5).value)
    print(lowest_ancestor1(h4, n4, n1).value)
    print(lowest_ancestor1(h4, n4, n3).value)
    print(lowest_ancestor1(h4, n4, n6).value)
    print(lowest_ancestor1(h4, n4, n7).value)
