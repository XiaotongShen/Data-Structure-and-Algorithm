# -*- coding: utf-8 -*-

"""
@File: Code04_RadixSort.py
@Author: Sarah Shen
@Time: 19/10/2022 11:27
"""
import sys
import math


# 基数排序，only for non-negative value
class RadixSort:

    def radix_sort(self, arr: list):
        if arr is None or len(arr) < 2:
            return
        self.sort(arr, 0, len(arr) - 1, self.max_bits(arr))

    def sort(self, arr: list, left: int, right: int, digit: int):
        radix = 10  # 基数是10
        # 有多少个数，需要准备多少个辅助空间
        assist = [0] * (right - left + 1)
        for d in range(1, digit + 1):
            # print("当前的d：%i" % d)
            # 有多少位就进出几次
            # 10个辅助空间
            # count[0] 当前位（d位）是0的数字有多少个
            # count[1] 当前位（d位）是（0和1）的数字有多少个
            # count[2] 当前位（d位）是（0，1，2）0的数字有多少个
            # count[i] 当前位（d位）是（0~i)的数字有多少个
            count = [0] * radix  # count[0,1,..., 9]
            for i in range(left, right + 1):
                # 从left到right遍历arr，检查d位置的数字，在count中对应数字index中 + 1
                j = self.get_digit(arr[i], d)
                # print(i, j)
                count[j] += 1
            # print(count)
            for i in range(1, radix):
                # count数组转换成前缀和
                count[i] = count[i - 1] + count[i]
            # print(count)
            for i in range(right, left - 1, -1):
                # 从右往左遍历arr, 找到元素d位置上的数，
                # 并找到小于等于该数的最右的位置，将元素放入辅助数组该位置
                j = self.get_digit(arr[i], d)
                assist[count[j] - 1] = arr[i]
                count[j] -= 1
                # print(i, arr[i], j, assist)
            # print(j, assist)
            j = 0
            for i in range(left, right + 1):
                # 用辅助数组替换原数组
                arr[i] = assist[j]
                j += 1

    @staticmethod
    def max_bits(arr: list) -> int:
        max_value = -sys.maxsize - 1  # 初始化最大值
        for element in arr:
            max_value = max(max_value, element)
        ans = 0
        while max_value != 0:
            ans += 1
            max_value /= 10
            max_value = int(max_value)
        return ans

    @staticmethod
    def get_digit(x: int, d: int):
        return int((x / int(math.pow(10, d - 1))) % 10)


if __name__ == "__main__":
    # a = 10908
    # res = 0
    # while a != 0:
    #     res += 1
    #     print(a)
    #     a /= 10
    #     a = int(a)
    # print(res)

    b = [103, 12, 11, 110, 101]
    print(b)
    rs = RadixSort()
    rs.radix_sort(b)
    print(b)
