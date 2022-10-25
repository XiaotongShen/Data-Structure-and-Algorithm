# -*- coding: utf-8 -*-

"""
@File: Code01_FriendCircles.py
@Author: Sarah Shen
@Time: 23/10/2022 00:26
"""


# 本题为leetcode原题
# 测试链接：https://leetcode.com/problems/friend-circles/
# 可以直接通过

def find_circle_num(m):
    n = len(m)
    union_find = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):
            if m[i][j] == 1:
                union_find.union(i, j)
    return union_find.sets


class UnionFind:

    def __init__(self, n: int):
        self.parent = [0] * n
        self.size = [0] * n
        self.help = [0] * n
        self.sets = n
        for i in range(n):
            self.parent[i] = i
            self.size[i] = 1

    # 从i开始一直往上，往上到不能再往上，代表节点，返回
    def find(self, i):
        hi = 0
        while i != self.parent[i]:
            self.help[hi] = i
            i = self.parent[i]
            hi += 1
        for hi in range(hi, -1, -1):
            self.parent[hi] = i
        return i

    def union(self, i, j):
        f1 = self.find(i)
        f2 = self.find(j)
        if f1 != f2:
            if self.size[f1] >= self.size[f2]:
                self.size[f1] += self.size[f2]
                self.parent[f2] = f1
            else:
                self.size[f2] += self.size[f1]
                self.parent[f1] = f2
            self.sets -= 1

    def sets(self):
        return self.sets
