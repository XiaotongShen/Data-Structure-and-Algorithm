# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/17.
Author: 
    Sarah Shen
Date: 
    2022/8/17
"""

# MergeSort
# 归并排序的递归方法和非递归方法

# 递归版本的并归排序
# 定义两个函数：
# process递归对数组的左右两部分排序
# merge对排好序的两部分进行merge，左右两个指针，各取出一个数比大小，小的放入辅助数组 & 指针移动到下一个。当指针越界的时候，将另一个部分剩余的部分放入辅助数组


class MergeSort:

    def process(self, x: list):
        if x is None or len(x) <= 1:
            return x
        else:
            n = len(x)
            m = n >> 1
            left = x[0:m]
            right = x[m:n]
            left = self.process(left)
            right = self.process(right)
            sorted_list = self.merge(left, right)
            return sorted_list

    def merge(self, left: list, right: list):
        assist = []
        p1 = 0
        p2 = 0
        left_n = len(left) - 1
        right_n = len(right) - 1

        while p1 <= left_n and p2 <= right_n:
            if left[p1] <= right[p2]:
                assist.append(left[p1])
                p1 += 1
            else:
                assist.append(right[p2])
                p2 += 1
        while p1 <= left_n:
            assist.append(left[p1])
            p1 += 1
        while p2 <= right_n:
            assist.append(right[p2])
            p2 += 1
        return assist


if __name__ == '__main__':
    a = [4, 3, 1, 0, 2, 5, 6, 0, 1, 2]
    b = [5, 2, 3, 1]
    print(a)
    ms = MergeSort()
    print(ms.process(a))
    print(b)
    ms = MergeSort()
    print(ms.process(b))
