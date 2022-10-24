# -*- coding: utf-8 -*-

"""
@File: Code05_UnionFind.py
@Author: Sarah Shen
@Time: 23/10/2022 00:25
"""


class Node:

    def __init__(self, v):
        self.value = v


class UnionFind:

    def __init__(self, values: list):
        self.nodes = dict()
        self.parents = dict()
        self.size_map = dict()
        for cur in values:
            node = Node(cur)
            self.nodes[cur] = node
            self.parents[node] = node
            self.size_map[node] = 1

    # 给你一个节点，请你往上到不能再往上，把代表节点返回
    def find_father(self, cur):
        path = list()
        while cur != self.parents.get(cur):
            path.append(cur)
            cur = self.parents.get(cur)
        while len(path) != 0:
            self.parents[path.pop()] = cur
        return cur

    def is_same_set(self, a, b):
        return self.find_father(self.nodes.get(a)) == self.find_father(self.nodes.get(b))

    def union(self, a, b):
        a_head = self.find_father(self.nodes.get(a))
        b_head = self.find_father(self.nodes.get(b))
        if a_head != b_head:
            a_setsize = self.size_map.get(a_head)
            b_setsize = self.size_map.get(b_head)
            big = a_head if a_setsize >= b_setsize else b_head
            small = b_head if big == a_head else b_head
            self.parents[small] = big
            self.size_map[big] = a_setsize + b_setsize
            self.size_map.pop(small)


if __name__ == '__main__':
    d = dict()
    d[1] = 'a'
    d[2] = 'b'
    print(d)
    print(d.pop(2))
    print(d)
