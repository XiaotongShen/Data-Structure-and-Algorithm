# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/29.
Author: 
    Sarah Shen
Date: 
    2022/8/29
"""
# 这里解决的问题是：
# 1. 数组中，只有一种数出现了奇数次
# 2. 数组中，有两种树出现了奇数次


def print_odd_times_num1(arr: list):
    eor = 0
    for i in range(len(arr)):
        eor ^= arr[i]
    print(eor)


def print_odd_times_num2(arr: list):
    eor = 0
    for i in range(len(arr)):
        eor ^= arr[i]
    right_one = eor & (-eor)    # 提取出最右的1

    eor_half = 0
    for i in range(len(arr)):
        if arr[i] & right_one != 0:
            eor_half ^= arr[i]
    print(eor_half, " ", eor_half ^ eor)


if __name__ == '__main__':
    arr1 = [3, 3, 2, 3, 1, 1, 1, 3, 1, 1, 1]
    arr2 = [4, 3, 4, 2, 2, 2, 4, 1, 1, 1, 3, 3, 1, 1, 1, 4, 2, 2]

    print_odd_times_num1(arr1)
    print_odd_times_num2(arr2)
