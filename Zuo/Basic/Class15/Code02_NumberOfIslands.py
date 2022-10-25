# -*- coding: utf-8 -*-

"""
@File: Code02_NumberOfIslands.py
@Author: Sarah Shen
@Time: 23/10/2022 00:26
"""


# 本题为leetcode原题
# 测试链接：https://leetcode.com/problems/number-of-islands/
# 所有方法都可以直接通过


# 感染的方式找到岛
def num_island3(board):
    islands = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '1':
                islands += 1
                infect(board, i, j)
    return islands


def infect(board, i, j):
    if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or board != 1:
        return
    board[i][j] = 2
    infect(board, i - 1, j)
    infect(board, i + 1, j)
    infect(board, i, j - 1)
    infect(board, i, j + 1)


# 并查集方式1
def num_island1(board):
    rows = len(board)
    cols = len(board[0])
    dots = [[None] * cols] * rows
    dot_list = list()
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == '1':
                dots[i][j] = Dot(None)
                dot_list.append(dots[i][j])
    uf = UnionFind1(dot_list)
    for j in range(1, cols):
        if board[0][j - 1] == '1' and board[0][j] == '1':
            uf.union(dots[0][j - 1], dots[0][j])
    for i in range(1, rows):
        if board[i - 1][0] == '1' and board[i][0] == '1':
            uf.union(dots[i - 1][0], dots[i][0])
    for i in range(1, rows):
        for j in range(1, cols):
            if board[i][j] == '1':
                if board[i][j - 1] == '1':
                    uf.union(dots[i][j], dots[i][j - 1])
                if board[i - 1][j] == '1':
                    uf.union(dots[i][j], dots[i - 1][j])
    return uf.sets


class Dot:

    def __init__(self, v):
        self.value = v


class Node:

    def __init__(self, v):
        self.value = v


class UnionFind1:

    def __init__(self, values):
        self.nodes = dict()
        self.parents = dict()
        self.size_map = dict()
        for cur in values:
            node = Node(cur)
            self.nodes[cur] = node
            self.parents[node] = node
            self.size_map[node] = 1

    def find_father(self, cur):
        path = list()
        while cur != self.parents[cur]:
            path.append(cur)
            cur = self.parents[cur]
        while len(path) != 0:
            self.parents[path.pop()] = cur
        return cur

    def union(self, a, b):
        a_head = self.find_father(self.nodes[a])
        b_head = self.find_father(self.nodes[b])
        if a_head != b_head:
            a_set_size = self.size_map[a_head]
            b_set_size = self.size_map[b_head]
            big = a_head if a_set_size >= b_set_size else b_set_size
            small = b_head if big == a_head else a_head
            self.parents[small] = big
            self.size_map[big] = a_set_size + b_set_size
            self.size_map.pop(small)

    def sets(self):
        return len(self.size_map)


# 并查集方式2
def num_island2(board):
    rows = len(board)
    cols = len(board[0])
    uf = UnionFind2(board)
    for j in range(1, cols):
        if board[0][j - 1] == '1' and board[0][j] == '1':
            uf.union(0, j - 1, 0, j)
    for i in range(1, rows):
        if board[i - 1][0] == '1' and board[i][0] == '1':
            uf.union(i - 1, 0, 0, 0)
    for i in range(1, rows):
        for j in range(1, cols):
            if board[i][j] == '1':
                if board[i][j - 1] == '1':
                    uf.union(i, j, i, j - 1)
                if board[i - 1][j] == '1':
                    uf.union(i, j, i - 1, j)
    return uf.sets


class UnionFind2:

    def __init__(self, board):
        self.cols = len(board[0])
        self.sets = 0
        rows = len(board)
        lens = rows * self.cols
        self.parent = [0] * lens
        self.size = [0] * lens
        self.help = [0] * lens
        for r in range(rows):
            for c in range(self.cols):
                if board[rows][self.cols] == '1':
                    idx = self.index(r, c)
                    self.parent[idx] = idx
                    self.size[idx] = 1
                    self.sets += 1

    def index(self, r, c):
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
        i1 = self.index(r1, c1)
        i2 = self.index(r2, c2)
        f1 = self.find(i1)
        f2 = self.find(i2)
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


if __name__ == '__main__':
    p = list()
