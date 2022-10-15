# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/9/1.
Author:
    Sarah Shen
Date:
    2022/9/1
"""


class SmallSum:

    def small_sum(self, arr: list):
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
        ast = []
        ans = 0
        p1 = lower
        p2 = mid + 1
        while p1 <= mid and p2 <= upper:
            if arr[p1] < arr[p2]:
                ans = ans + arr[p1] * (upper - p2 + 1)
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
                    ans += arr[j] if arr[j] < arr[i] else 0
            return ans


if __name__ == '__main__':
    a = [1, 3, 4, 5, 2, 4, 6, 7]
    b = [1, 3, 6, 2, 7, 0, 9, 8, 5, 2, 4, 6, 7]

    t = Test()
    s = SmallSum()

    print(a)
    print(t.comparator(a))
    print(s.small_sum(a))

    print(b)
    print(t.comparator(b))
    print(s.small_sum(b))
