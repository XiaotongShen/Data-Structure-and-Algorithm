# -*- coding: utf-8 -*-

"""
@File: Code02_AllLessNumSubArray.py
@Author: Sarah Shen
@Time: 31/10/2022 22:46
"""
import random

"""
给定一个整型数组arr, 和一个整数num
arr中的子数组如果想达标，就必须满足sub中的最大值与最小值的差要小于num
返回arr中达标子数组的数量
"""


# 暴力方法
def right_base(arr: [int], num: int):
    if arr is None or len(arr) == 0 or num < 0:
        return 0
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i, n):
            max_v = arr[i]
            min_v = arr[i]
            for k in range(i + 1, j + 1):
                max_v = max(max_v, arr[k])
                min_v = min(min_v, arr[k])
            if max_v - min_v <= num:
                count += 1
    return count


def all_less_num(arr: [int], num: int):
    if arr is None or len(arr) == 0 or num < 0:
        return 0
    n = len(arr)
    count = 0
    max_window = list()
    min_window = list()
    right = 0
    for left in range(n):
        while right < n:
            while len(max_window) != 0 and arr[max_window[-1]] <= arr[right]:
                max_window.pop()
            max_window.append(right)
            while len(min_window) != 0 and arr[min_window[-1]] >= arr[right]:
                min_window.pop()
            min_window.append(right)
            if arr[max_window[0]] - arr[min_window[0]] > num:
                break
            else:
                right += 1
        count += right - left
        if max_window[0] == left:
            max_window.remove(max_window[0])
        if min_window[0] == left:
            min_window.remove(min_window[0])
    return count


def generate_random_array(max_l: int, max_v: int):
    n = int(random.random() * (max_l + 1))
    arr = [0] * n
    for i in range(n):
        arr[i] = int(random.random() * (max_v + 1))
    return arr


if __name__ == '__main__':
    max_len = 10
    max_value = 20
    test_times = 100
    print('Test Start')
    for i in range(test_times):
        rand_arr = generate_random_array(max_len, max_value)
        rand_num = int(random.random() * (max_value + 1))
        ans1 = right_base(rand_arr, rand_num)
        ans2 = all_less_num(rand_arr, rand_num)
        if ans1 != ans2:
            print('Oops!')
            print(rand_arr, rand_num)
            print(ans1)
            print(ans2)
            break
    print('Test Finish')
