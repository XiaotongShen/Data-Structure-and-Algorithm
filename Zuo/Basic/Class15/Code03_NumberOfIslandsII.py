# -*- coding: utf-8 -*-

"""
@File: Code03_NumberOfIslandsII.py
@Author: Sarah Shen
@Time: 23/10/2022 00:26
"""


# 本题为leetcode原题
# 测试链接：https://leetcode.com/problems/number-of-islands-ii/
# 所有方法都可以直接通过


def num_islands21(m, n, positions):
    uf = UnionFind1(m, n)
    ans = list()
    for position in positions:
        ans.apend(uf.connect(position[0], position[1]))
    return ans


class UnionFind:

    def __init__(self, m, n):
        self.rows = m
        self.cols = n
        self.sets = 0
        self.lens = self.rows * self.cols
        self.parent = [0] * self.lens
        self.size = [0] * self.lens
        self.help = [0] * self.lens

    def index(self, r: int, c: int):
        return r * self.cols + c

    def find(self, i):
        hi = 0
        while i != self.parent[i]:
            self.help[hi] = i
            hi += 1
            i = self.parent[i]
        for hi in range(hi, -1, -1):
            self.parent[hi] = i

        return i

    def union(self, r1, c1, r2, c2):
        if r1 < 0 or r1 == self.rows or r2 < 0 or r2 == self.rows or c1 < 0 or c1 == self.cols or c2 < 0 or c2 == self.cols:
            return
        i1 = self.index(r1, c1)
        i2 = self.index(r2, c2)
        f1 = self.find(i1)
        f2 = self.find(i2)
        if self.size[f1] >= self.size[f2]:
            self.size[f1] += self.size[f2]
            self.parent[f2] = f1
        else:
            self.size[f2] += self.size[f1]
            self.parent[f1] = f2
        self.sets -= 1

    def connect(self, r: int, c: int):
        idx = self.index(r, c)
        if self.size[idx] == 0:
            self.parent[idx] = idx
            self.size[idx] = 1
            self.sets += 1
            self.union(r - 1, c, r, c)
            self.union(r + 1, c, r, c)
            self.union(r, c - 1, r, c)
            self.union(r, c + 1, r, c)
        return self.sets


# 课上讲的如果 m * n比较大，会经历很重的初始化，而k比较小，怎么优化的方法
# 以下省略
