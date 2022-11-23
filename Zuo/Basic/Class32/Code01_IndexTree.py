# -*- coding: utf-8 -*-

"""
@File: Code01_IndexTree.py
@Author: Sarah Shen
@Time: 23/11/2022 14:39
"""
import random


class IndexTree:

    def __init__(self, size: int):
        self.n = size
        self.tree = [0] * (self.n + 1)

    def sum(self, idx: int):
        """
        1~idx 累加和是多少？
        """
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

    def add(self, idx: int, d: int):
        """
        idx & -idx :  提取出idx最右侧的1出来
        idx ：          0011001000
        idx & -idx :   0000001000
        """
        while idx <= self.n:
            self.tree[idx] += d
            idx += idx & -idx


class Right:
    """
    用于比较的正确的算法过程
    """

    def __init__(self, size: int):
        self.n = size + 1
        self.nums = [0] * (self.n + 1)

    def sum(self, idx: int):
        res = 0
        for i in range(idx + 1):
            res += self.nums[i]
        return res

    def add(self, idx: int, d: int):
        self.nums[idx] += d


if __name__ == '__main__':
    max_size = 100
    max_value = 100
    test_times = 20000
    tree = IndexTree(max_size)
    test = Right(max_size)
    print('Test Begin')
    for i in range(test_times):
        idx = int(random.random() * max_size) + 1
        if random.random() < 0.5:
            add = int(random.random() * max_value)
            tree.add(idx, add)
            test.add(idx, add)
        else:
            if tree.sum(idx) != test.sum(idx):
                print("Oops!")
    print("Test Finish!")
