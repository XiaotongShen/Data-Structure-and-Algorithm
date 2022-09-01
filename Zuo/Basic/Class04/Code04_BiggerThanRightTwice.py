# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/9/1.
Author: 
    Sarah Shen
Date: 
    2022/9/1
"""


class BiggerThanRightTwice:

    def revers_pair(self, arr: list):
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
        if lower == upper:
            return 0
        else:
            ans = 0
            window_r = mid + 1
            for i in range(lower, mid + 1, 1):
                while window_r < upper and arr[i] > arr[window_r] * 2:
                    window_r += 1
                ans += window_r - mid - 1
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
                    ans += 1 if arr[j] > 2 * arr[i] else 0
            return ans


if __name__ == '__main__':
    a = [1, 3, 5, 13, 17, 19, 2, 4, 6, 8, 10, 12]
    b = a.copy()
    t = Test()
    r = BiggerThanRightTwice()

    print(a)
    print(t.comparator(a))
    print(a)

    print(b)
    print(r.revers_pair(b))
    print(b)
