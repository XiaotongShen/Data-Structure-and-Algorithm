# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/26.
Author: 
    Sarah Shen
Date: 
    2022/8/26
"""
import random


class BubbleSort:
    """
    冒泡排序基本思路
    0 ~ N-1 区间两两比较，大的向后移
    0 ~ N-2 区间两江比较，大的向后移
    0 ~ N-3 区间两两比较，大的向后移
    ...
    """

    def main(self, arr: list):
        if arr is None or len(arr) < 2:
            return arr
        else:
            for i in range(len(arr), 1, -1):
                for j in range(i - 1):
                    if arr[j] >= arr[j + 1]:
                        self.swap(arr, j, j + 1)
                    else:
                        pass
            return arr

    @staticmethod
    def swap(arr: list, i: int, j: int):
        arr[i] = arr[i] ^ arr[j]
        arr[j] = arr[i] ^ arr[j]
        arr[i] = arr[i] ^ arr[j]


class Test:
    """ 对数器：随机生成数组，比较两个不同的排序算法结果是否一致 """

    @staticmethod
    def generate_random_array(max_len, max_val):
        cur_len = int(random.random() * max_len)
        arr = []
        for i in range(cur_len):
            arr.append(int(random.random() * max_val))
        return arr

    @staticmethod
    def comparator(arr):
        arr.sort()
        return arr

    def main(self, times: int, max_len: int, max_val: int, func):
        succeed = True
        for i in range(times):
            arr = self.generate_random_array(max_len, max_val)
            arr1 = arr.copy()
            arr2 = arr.copy()
            func(arr1)
            self.comparator(arr2)
            if arr1 != arr2:
                succeed = False
                print(arr)
                print(arr1)
                print(arr2)
                break
        print("Nice!" if succeed else "Oops, Something is Wrong!")


if __name__ == '__main__':
    test = Test()
    sort = BubbleSort()

    test.main(times=100000, max_len=10, max_val=10, func=sort.main)
