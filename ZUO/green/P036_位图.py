# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/5.
Author: 
    Sarah Shen
Date: 
    2022/8/5
"""


class BitMap:

    def __init__(self, num_max):
        self.size = int((num_max + 32) >> 5)
        self.array = [0 for i in range(self.size)]

    def add(self, val):
        self.array[val >> 5] |= (int(1) << (val & 31))

    def delete(self, val):
        self.array[val >> 5] &= ~(int(1) << (val & 31))

    def contains(self, val):
        return self.array[val >> 5] & (int(1) << (val & 31)) != 0


if __name__ == '__main__':
    a = 100

    print(int(a / 32))  # 数值运算
    print(a >> 5)   # 位运算
    print(a % 32)   # 数值运算
    print(a & 31)   # 位运算

    bm = BitMap(200)
    print(bm.array)

    bm.add(76)
    print(bm.array)
    print(bm.contains(76))

    bm.delete(76)
    print(bm.array)
    print(bm.contains(82))
