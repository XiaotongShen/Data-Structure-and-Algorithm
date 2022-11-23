# -*- coding: utf-8 -*-

"""
@File: Code02_FallingSquares.py
@Author: Sarah Shen
@Time: 08/11/2022 18:23
"""


class SegmentTree:

    def __init__(self, size: int):
        n = size + 1
        self.max = [0] * (n << 2)
        self.change = [0] * (n << 2)
        self.update = [False] * (n << 2)

    def push_up(self, rt: int):
        self.max[rt] = max(self.max[rt << 1], self.max[rt << 1 | 1])

    def push_down(self, rt: int, ln: int, rn: int):
        if self.update[rt]:
            self.update[rt << 1] = True
            self.update[rt << 1 | 1] = True
            self.change[rt << 1] = self.change[rt]
            self.change[rt << 1 | 1] = self.change[rt]
            self.max[rt << 1] = self.change[rt]
            self.max[rt << 1 | 1] = self.change[rt]
            self.update[rt] = False

    def tree_update(self, big_l: int, big_r: int, c: int, l: int, r: int, rt: int):
        if big_l <= l and r <= big_r:
            self.update[rt] = True
            self.change[rt] = c
            self.max[rt] = c
            return
        mid = (l + r) >> 1
        self.push_down(rt, mid - l + 1, r - mid)
        if big_l <= mid:
            self.tree_update(big_l, big_r, c, l, mid, rt << 1)
        if big_r > mid:
            self.tree_update(big_l, big_r, c, mid + 1, r, rt << 1 | 1)
        self.push_up(rt)

    def query(self, big_l: int, big_r: int, l: int, r: int, rt: int):
        if big_l <= l and r <= big_r:
            return self.max[rt]
        mid = (l + r) >> 1
        self.push_down(rt, mid - l + 1, r - mid)
        left = 0
        right = 0
        if big_l <= mid:
            left = self.query(big_l, big_r, l, mid, rt << 1)
        if big_r > mid:
            right = self.query(big_l, big_r, mid + 1, r, rt << 1 | 1)
        return max(left, right)

    def index(self, positions:[list]):
        # TODO


    def falling_squares(self, positions: [list]):
        # TODO

