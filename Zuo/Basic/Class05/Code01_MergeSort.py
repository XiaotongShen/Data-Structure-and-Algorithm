# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/9/1.
Author: 
    Sarah Shen
Date: 
    2022/9/1
"""


class Solution1:
    """ MergeSort 的递归写法 """

    def merge_sort(self, arr: list):
        if arr is None or len(arr) < 2:
            return
        else:
            self.process(arr, 0, len(arr) - 1)

    def process(self, arr: list, lower: int, upper: int):
        if lower == upper:
            return
        else:
            mid = lower + ((upper - lower) >> 1)
            self.process(arr, lower, mid)
            self.process(arr, mid + 1, upper)
            self.merge(arr, lower, mid, upper)

    @staticmethod
    def merge(arr: list, lower: int, mid: int, upper: int):
        ast = []
        p1 = lower
        p2 = mid + 1
        while p1 <= mid and p2 <= upper:
            if arr[p1] <= arr[p2]:
                ast.append(arr[p1])
                p1 += 1
            else:
                ast.append(arr[p2])
                p2 += 1
        while p1 <= mid:
            ast.append(arr[p1])
            p1 += 1
        while p2 <= upper:
            ast.append(arr[p2])
            p2 += 1
        for i in range(len(ast)):
            arr[lower + i] = ast[i]


class Solution2:
    """ MergeSort 的非递归写法 """

    def merge_sort(self, arr: list):
        if arr is None or len(arr) < 2:
            return
        else:
            n = len(arr)
            merge_size = 1
            # print(arr)
            while merge_size < n:
                # print("==========")
                lower = 0
                while lower < n:
                    if merge_size > n - lower:
                        break
                    mid = lower + merge_size - 1
                    upper = mid + min(merge_size, n - mid - 1)
                    self.merge(arr, lower, mid, upper)
                    lower = upper + 1
                # print(arr)
                if merge_size > n / 2:
                    break
                merge_size <<= 1

    @staticmethod
    def merge(arr: list, lower: int, mid: int, upper: int):
        ast = []
        p1 = lower
        p2 = mid + 1
        while p1 <= mid and p2 <= upper:
            if arr[p1] <= arr[p2]:
                ast.append(arr[p1])
                p1 += 1
            else:
                ast.append(arr[p2])
                p2 += 1
        while p1 <= mid:
            ast.append(arr[p1])
            p1 += 1
        while p2 <= upper:
            ast.append(arr[p2])
            p2 += 1
        for i in range(len(ast)):
            arr[lower + i] = ast[i]


# 对数器待完成

if __name__ == '__main__':
    a = [1, 3, 4, 5, 2, 4, 6, 7]
    b = [1, 3, 6, 2, 7, 0, 9, 8, 5, 2, 4, 6, 7]

    s1 = Solution1()
    print(a)
    s1.merge_sort(a)
    print(a)

    s2 = Solution2()
    print(b)
    s2.merge_sort(b)
    print(b)
