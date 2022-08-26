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


class SortTest:
    """ 排序算法的对数器，随机生成数组，比较两个不同的排序算法结果是否一致 """
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

    @staticmethod
    def generate_random_array(max_len, max_val):
        cur_len = int(random.random()*max_len)
        arr = []
        for i in range(cur_len):
            arr.append(int(random.random()*max_val))
        return arr

    @staticmethod
    def comparator(arr):
        arr.sort()
        return arr


class SelectSort:
    """
    选择排序思路：
    0 ~ N-1 找到最小值，放到0位置上
    1 ~ N-1 找到最小值，放到1位置上
    2 ~ N-1 找到最小值，放到2位置上
    ...
    """
    def main(self, arr: list):
        if arr is None or len(arr) < 2:
            return arr
        else:
            for i in range(len(arr)):
                min_index = i
                for j in range(i, len(arr)):
                    if arr[j] <= arr[min_index]:
                        min_index = j
                self.swap(arr, i, min_index)
            return arr

    @staticmethod
    def swap(arr: list, i: int, j: int):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


if __name__ == '__main__':

    select = SelectSort()
    test = SortTest()

    test.main(times=100000, max_len=10, max_val=10, func=select.main)
