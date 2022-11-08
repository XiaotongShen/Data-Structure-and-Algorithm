# -*- coding: utf-8 -*-

"""
@File: Code01_FindMinKth.py
@Author: Sarah Shen
@Time: 08/11/2022 11:40
"""
import random
from queue import PriorityQueue


def min_kth1(arr: list, k: int):
    """ 利用大跟堆，时间复杂度O(N * logK) """
    max_heap = PriorityQueue()
    for i in range(k):
        max_heap.put((-arr[i], arr[i]))  # 以arr数组中的值倒序排序放入小根堆
    for i in range(k, len(arr)):
        if arr[i] < max_heap.queue[-1][1]:
            max_heap.get()
            max_heap.put((-arr[i], arr[i]))
    return max_heap.queue[-1][1]


def min_kth2(array: list, k: int):
    """ 改写快排，时间复杂度O(N) """
    arr = array.copy()
    return process2(arr, 0, len(arr) - 1, k - 1)


def process2(arr: list, left: int, right: int, idx: int):
    if left == right:
        return arr[left]
    pivot = arr[left + int(random.random() * (right - left + 1))]
    ran = partition(arr, left, right, pivot)
    if ran[0] <= idx <= ran[1]:
        return arr[idx]
    elif idx < ran[0]:
        return process2(arr, left, ran[0] - 1, idx)
    else:
        return process2(arr, ran[1] + 1, right, idx)


def partition(arr: list, left: int, right: int, pivot: int):
    less = left - 1
    more = right + 1
    cur = left
    while cur < more:
        if arr[cur] < pivot:
            less += 1
            swap(arr, less, cur)
            cur += 1
        elif arr[cur] > pivot:
            more -= 1
            swap(arr, cur, more)
        else:
            cur += 1
    return [less + 1, more - 1]


def swap(arr: list, i1: int, i2: int):
    tmp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = tmp


def min_kth3(array: list, k: int):
    """ 利用bfprt算法，时间复杂度O(N) """
    arr = array.copy()
    return bfprt(arr, 0, len(arr) - 1, k - 1)


def bfprt(arr: list, left: int, right: int, idx: int):
    if left == right:
        return arr[left]
    pivot = median_of_medians(arr, left, right)
    ran = partition(arr, left, right, pivot)
    if ran[0] <= idx <= ran[1]:
        return arr[idx]
    elif idx < ran[0]:
        return bfprt(arr, left, ran[0] - 1, idx)
    else:
        return bfprt(arr, ran[1] + 1, right, idx)


def median_of_medians(arr: list, left: int, right: int):
    """
    left ...right 每5个数一组
    每一个小组内部排好序
    小组的中位数组成新的数组
    这个新数组的中位数返回
    """
    size = right - left + 1
    offset = 0 if size % 5 == 0 else 1
    m_arr = [0] * (int(size / 5) + offset)
    for team in range(len(m_arr)):
        team_first = left + team * 5
        # left ... left +4
        # left + 5 ... left + 9
        # left +10 ... left + 14
        m_arr[team] = get_median(arr, team_first, min(right, team_first + 4))
    # 从m_arr中找到中位数
    return bfprt(m_arr, 0, len(m_arr) - 1, int(len(m_arr) / 2))


def get_median(arr: list, left: int, right: int):
    insertion_sort(arr, left, right)
    return arr[int((left + right) / 2)]


def insertion_sort(arr: list, left: int, right: int):
    for i in range(left + 1, right + 1):
        j = i - 1
        while j >= left and arr[j] > arr[j + 1]:
            swap(arr, j, j + 1)
            j -= 1


def get_random_array(max_size: int, max_value: int):
    arr = [0] * int(random.random() * max_size + 1)
    for i in range(len(arr)):
        arr[i] = int(random.random() * (max_value + 1))
    return arr


if __name__ == '__main__':
    max_size = 100
    max_value = 100
    test_times = 10000
    print('test begin')
    for i in range(test_times):
        rand_arr = get_random_array(max_size, max_value)
        rand_k = int(random.random() * len(rand_arr)) + 1
        ans1 = min_kth1(rand_arr, rand_k)
        ans2 = min_kth2(rand_arr, rand_k)
        ans3 = min_kth3(rand_arr, rand_k)
        if ans1 != ans2 and ans2 != ans3:
            print('Oops!')
            print(rand_arr, rand_k)
            print(ans1)
            print(ans2)
            print(ans3)
            break
    print('test finish')
