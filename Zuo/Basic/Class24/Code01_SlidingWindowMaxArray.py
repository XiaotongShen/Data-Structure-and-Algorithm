# -*- coding: utf-8 -*-

"""
@File: Code01_SlidingWindowMaxArray.py
@Author: Sarah Shen
@Time: 31/10/2022 22:45
"""
import random


# 暴力方法遍历
def right_base(arr: [int], w: int):
    if arr is None or w < 1 or len(arr) < w:
        return None
    n = len(arr)
    res = [0] * (n - w + 1)
    idx = 0
    left = 0
    right = w - 1
    while right < n:
        max_value = arr[left]
        for i in range(left + 1, right + 1):
            max_value = max(max_value, arr[i])
        res[idx] = max_value
        idx += 1
        left += 1
        right += 1
    return res


def get_max_window(arr: [int], w: int):
    if arr is None or w < 1 or len(arr) < w:
        return None
    q_max = list()  # q_max:窗口最大值的更新结构
    res = [0] * (len(arr) - w + 1)
    idx = 0
    for right in range(len(arr)):
        while len(q_max) != 0 and arr[q_max[-1]] <= arr[right]:
            q_max.pop()
        q_max.append(right)
        if q_max[0] == right - w:  # 最早放入的index失效，弹出第一个值
            q_max.remove(q_max[0])
        if right >= w - 1:
            res[idx] = arr[q_max[0]]
            idx += 1
    return res


def generate_array(max_l: int, max_v: int):
    n = int(random.random() * max_l)
    arr = [0] * n
    for i in range(n):
        arr[i] = int(random.random() * max_v)
    return arr


def is_equal(arr1: [int], arr2: [int]):
    if (arr1 is None and arr2 is not None) or (arr1 is not None and arr2 is None):
        return False
    if arr1 is None and arr2 is None:
        return True
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True


if __name__ == '__main__':
    test_times = 10000
    max_size = 100
    max_value = 100
    print('Test Start')
    for i in range(test_times):
        rand_arr = generate_array(max_size, max_value)
        rand_w = int(random.random() * (len(rand_arr) + 1))
        ans1 = right_base(rand_arr, rand_w)
        ans2 = get_max_window(rand_arr, rand_w)
        if not is_equal(ans1, ans2):
            print('Oops!')
            print(rand_arr, rand_w)
            print(ans1)
            print(ans2)
            break
    print('Test Finish')
