# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/31.
Author:
    Sarah Shen
Date:
    2022/8/31
"""


class GetMax:
    """ 使用递归的方法，求arr中的最大值 """

    def main(self, arr: list):
        if arr is None or len(arr) < 1:
            return None
        else:
            return self.process(arr)

    def process(self, arr: list):
        # print(arr)
        if len(arr) == 1:
            return arr[0]
        else:
            lower = 0
            upper = len(arr)
            mid = lower + ((upper - lower) >> 1)
            left_max = self.process(arr[lower:mid])
            right_max = self.process(arr[mid:upper])
            return max(left_max, right_max)


if __name__ == '__main__':
    a = [7, 8, 9, 2, 3, 51, 0, 233, 4, 2, 66, 8, 6, 35, 45, 67, 88]
    b = [1]
    c = []
    test = GetMax()
    print(test.main(a))
    print(test.main(b))
    print(test.main(c))
