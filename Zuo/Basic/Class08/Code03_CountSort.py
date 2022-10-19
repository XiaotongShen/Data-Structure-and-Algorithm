# -*- coding: utf-8 -*-

"""
@File: Code03_CountSort.py
@Author: Sarah Shen
@Time: 19/10/2022 11:27
"""
import sys


# 计数排序，only for 0 ~ 200 value
def count_sort(arr: list):
    # 边界条件，不需要排序的情况
    if arr is None or len(arr) < 2:
        return
    # 获取数组中的最大值
    max_value = -sys.maxsize - 1
    for element in arr:
        max_value = max(max_value, element)
    # 创建长度为最大index为max_value的容器桶
    bucket = [0] * (max_value + 1)
    for element in arr:
        # 遍历数组中每一个整数，并在整数对应的index上 + 1
        bucket[element] += 1
        # bucket表示arr数组中每一个整数值(bucket中对应的index)出现的次数
    i = 0
    for j in range(len(bucket)):
        while bucket[j] > 0:
            arr[i] = j
            i += 1
            bucket[j] -= 1


if __name__ == "__main__":
    # max_v = -sys.maxsize - 1
    # min_v = sys.maxsize
    # print(max_v, min_v)

    a = [2, 4, 3, 5, 67, 8, 3, 4, 1, 0, 7, 4, 6, 6, 7, 3, 2]
    print(a)
    count_sort(a)
    print(a)
