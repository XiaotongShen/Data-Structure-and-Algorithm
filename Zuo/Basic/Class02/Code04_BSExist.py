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


def exist(arr: list, num: int):
    """ 在有序数组arr中，判断数num是否存在 """
    if arr is None or len(arr) < 1:
        return False
    else:
        li = 0
        ri = len(arr) - 1
        while li < ri:
            mid = li + ((ri - li) >> 1)
            if arr[mid] == num:
                return True
            elif arr[mid] > num:
                ri = mid - 1
            else:
                li = mid + 1
        return arr[li] == num  # 如果不符合while的条件，仅剩的情况为li == ri, 即数组中只有一个位置伤的数需要判断，那么只需要判断这一个位置上的数是否等于num，返回结果即好


class Test:
    """ 对数器，随机生成数组，比较两个不同的算法结果是否一致 """

    @staticmethod
    def generate_random_array(max_len, max_val):
        cur_len = int(random.random() * max_len)
        arr = []
        for i in range(cur_len):
            arr.append(int(random.random() * max_val))
        return arr

    @staticmethod
    def comparator(arr: list, num: int):
        for cur in arr:
            if cur == num:
                return True
        return False

    def main(self, times: int, max_len: int, max_val: int, func):
        succeed = True
        for i in range(times):
            arr = self.generate_random_array(max_len, max_val)
            arr.sort()
            num = int(random.random() * max_val)
            ans1 = func(arr, num)
            ans2 = self.comparator(arr, num)
            if ans1 != ans2:
                succeed = False
                print(arr)
                print(num)
                break
        print("Nice!" if succeed else "Oops, Something is Wrong!")


if __name__ == '__main__':
    test = Test()
    test.main(times=500000, max_len=100, max_val=100, func=exist)
