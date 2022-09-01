# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/9/1.
Author: 
    Sarah Shen
Date: 
    2022/9/1
"""


class ReversePair:

    def reverse_pair_num(self, arr: list):
        if arr is None or len(arr) < 2:
            return 0
        else:
            return self.process(arr, 0, len(arr) - 1)

    def process(self, arr: list, lower: int, upper: int):
        if lower == upper:
            return 0
        else:
            mid = lower + ((upper - lower) >> 1)
            return \
                self.process(arr, lower, mid) + \
                self.process(arr, mid + 1, upper) + \
                self.merge(arr, lower, mid, upper)

    @staticmethod
    def merge(arr: list, lower: int, mid: int, upper: int):
        ans = 0
        ast = []
        p1 = mid
        p2 = upper
        while p1 >= lower and p2 >= mid + 1:
            if arr[p1] > arr[p2]:
                ast.append(arr[p1])
                ans += (p2 - mid)
                p1 -= 1
            else:
                ast.append(arr[p2])
                p2 -= 1
        while p1 >= lower:
            ast.append(arr[p1])
            p1 -= 1
        while p2 >= mid + 1:
            ast.append(arr[p2])
            p2 -= 1
        for i in range(len(ast)):
            arr[upper - i] = ast[i]
        return ans


class Test:
    """ 对数器待完成 """

    @staticmethod
    def comparator(arr: list):
        ans = 0
        if arr is None or len(arr) < 2:
            return ans
        else:
            for i in range(len(arr)):
                for j in range(i):
                    ans += 1 if arr[j] > arr[i] else 0
            return ans


if __name__ == '__main__':
    a = [1, 3, 5, 13, 17, 19, 2, 4, 6, 8, 10, 12]
    b = a.copy()
    t = Test()
    r = ReversePair()

    print(a)
    print(t.comparator(a))
    print(a)

    print(b)
    print(r.reverse_pair_num(b))
    print(b)
