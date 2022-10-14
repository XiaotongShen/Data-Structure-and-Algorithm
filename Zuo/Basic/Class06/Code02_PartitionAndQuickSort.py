# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/9/1.
Author:
    Sarah Shen
Date:
    2022/9/1
"""
import random


class PartitionAndQuickSort:

    @staticmethod
    def swap(arr: list, i: int, j: int):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def partition(self, arr: list, left: int, right: int):
        """ arr[left, ..., right]上，以arr[right]位置的数做划分，小于等于放左边，大于放右边 """
        if left > right:
            return -1
        elif left == right:
            return left
        else:
            less_equal = left - 1
            for i in range(left, right):
                if arr[i] <= arr[right]:
                    less_equal += 1
                    self.swap(arr, i, less_equal)
            less_equal += 1
            self.swap(arr, less_equal, right)
            return less_equal

    def netherlands_flag(self, arr: list, left: int, right: int):
        """ arr[left, ..., right]荷兰国旗的划分，以arr[right]位置的数做划分，< arr[R] == arr[R] > arr[R] """
        if left > right:
            return [-1, -1]
        elif left == right:
            return [left, right]
        else:
            less = left - 1
            more = right
            i = left
            while i < more:
                if arr[i] == arr[right]:
                    i += 1
                elif arr[i] < arr[right]:
                    less += 1
                    self.swap(arr, i, less)
                    i += 1
                else:
                    more -= 1
                    self.swap(arr, i, more)

            self.swap(arr, more, right)
            return [less + 1, more]

    def quick_sort_1(self, arr: list):
        if arr is None or len(arr) < 2:
            return
        else:
            self.process1(arr, 0, len(arr) - 1)

    def process1(self, arr: list, left: int, right: int):
        if left >= right:
            return
        else:
            mid = self.partition(arr, left, right)
            self.process1(arr, left, mid - 1)
            self.process1(arr, mid + 1, right)

    def quick_sort_2(self, arr: list):
        if arr is None or len(arr) < 2:
            return
        else:
            self.process2(arr, 0, len(arr) - 1)

    def process2(self, arr: list, left: int, right: int):
        if left >= right:
            return
        else:
            equal_area = self.netherlands_flag(arr, left, right)
            self.process2(arr, left, equal_area[0] - 1)
            self.process2(arr, equal_area[1] + 1, right)

    def quick_sort_3(self, arr: list):
        if arr is None or len(arr) < 2:
            return
        else:
            self.process3(arr, 0, len(arr) - 1)

    def process3(self, arr: list, left: int, right: int):
        if left >= right:
            return
        else:
            self.swap(arr, left + int(random.random() * (right - left + 1)), right)
            equal_area = self.netherlands_flag(arr, left, right)
            self.process3(arr, left, equal_area[0] - 1)
            self.process3(arr, equal_area[1] + 1, right)


class Test:
    """ 对数器待完成 """
    @staticmethod
    def generate_random_arr(max_len, max_val):
        cur_len = int(random.random() * max_len)
        arr = []
        for i in range(cur_len):
            arr.append(int(random.random() * max_val))
        return arr


if __name__ == '__main__':
    t = Test()
    qs = PartitionAndQuickSort()

    a = t.generate_random_arr(20, 20)
    b = a.copy()
    c = a.copy()
    d = a.copy()
    e = a.copy()

    # a = [2, 3, 4, 5, 2, 3, 4, 5, 2, 3]
    # b = [2, 3, 4, 5, 2, 3, 4, 5, 2, 3]

    # print(a)
    # qs.partition(a, 0, len(a) - 1)
    # print(a)
    # print("===========")
    # print(b)
    # r = qs.netherlands_flag(b, 0, len(b) - 1)
    # print(b)
    # print(r)
    # print(b[r[0]: r[1] + 1])

    print(c)
    qs.quick_sort_1(c)
    print(c)
    print("===========")
    print(d)
    qs.quick_sort_2(d)
    print(d)
    print(c == d)
    print("===========")
    print(e)
    qs.quick_sort_2(e)
    print(e)
    print(c == d == e)
