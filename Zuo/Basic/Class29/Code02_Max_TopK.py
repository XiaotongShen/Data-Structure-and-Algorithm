# -*- coding: utf-8 -*-

"""
@File: Code02_Max_TopK.py
@Author: Sarah Shen
@Time: 08/11/2022 11:41
"""
import random


def max_top_k1(arr: list, k: int):
    """
    时间复杂度O(N*logN)
    排序 + 收集
    """
    if arr is None or len(arr) == 0:
        return [0]
    n = len(arr)
    k = min(n, k)
    arr.sort()
    ans = [0] * k
    i = n - 1
    for j in range(k):
        ans[j] = arr[i]
        i -= 1
    return ans


def max_top_k2(arr: list, k: int):
    """
    时间复杂度O(N+K * logN)
    堆
    """
    if arr is None or len(arr) == 0:
        return [0]
    n = len(arr)
    k = min(k, n)
    # 从底向上建堆，时间复杂度O(N)
    for i in range(n - 1, -1, -1):
        heapify(arr, i, n)
    # 只把前k个数放在arr末尾，然后收集，O(K*logN)
    heap_size = n
    heap_size -= 1
    swap(arr, 0, heap_size)
    count = 1
    while heap_size > 0 and count < k:
        heapify(arr, 0, heap_size)
        heap_size -= 1
        swap(arr, 0, heap_size)
        count += 1
    ans = [0] * k
    i = n - 1
    for j in range(k):
        ans[j] = arr[i]
        i -= 1
    return ans


def heap_insert(arr: list, idx: int):
    while arr[idx] > arr[int((idx - 1) / 2)]:
        swap(arr, idx, int((idx - 1) / 2))
        idx = (idx - 1) / 2


def heapify(arr: list, idx: int, heap_size: int):
    left = idx * 2 + 1
    while left < heap_size:
        largest = left + 1 if left + 1 < heap_size and arr[left + 1] > arr[left] else left
        largest = largest if arr[largest] > arr[idx] else idx
        if largest == idx:
            break
        swap(arr, largest, idx)
        idx = largest
        left = idx * 2 + 1


def swap(arr: list, i: int, j: int):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def max_top_k3(arr: list, k: int):
    """
    方法3：时间复杂度O(N * logk)
    """
    if arr is None or len(arr) == 0:
        return [0]
    n = len(arr)
    k = min(k, n)
    # O(N)
    num = min_kth(arr, n - k)
    ans = [0] * k
    idx = 0
    for i in range(n):
        if arr[i] > num:
            ans[idx] = arr[i]
            idx += 1
    while idx < k:
        ans[idx] = num
        idx += 1
    ans.sort()
    left = 0
    right = k - 1
    while left < right:
        swap(ans, left, right)
        left += 1
        right -= 1
    return ans


def min_kth(arr: list, idx: int):
    left = 0
    right = len(arr) - 1
    while left < right:
        pivot = arr[left + int(random.random() * (right - left + 1))]
        ran = partition(arr, left, right, pivot)
        if idx < ran[0]:
            right = ran[0] - 1
        elif idx > ran[1]:
            left = ran[1] + 1
        else:
            return pivot
    return arr[left]


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


def get_random_array(max_size: int, max_value: int):
    arr = [0] * int(random.random() * (max_size + 1))
    for i in range(len(arr)):
        arr[i] = int(random.random() * (max_value + 1)) - int(random.random() * max_value)
    return arr


def is_equal(arr1: list, arr2: list):
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
    max_s = 100
    max_v = 100
    test_time = 50000
    print('测试开始')
    for i in range(test_time):
        k = int(random.random() * max_s) + 1
        arr = get_random_array(max_s, max_v)

        arr1 = arr.copy()
        arr2 = arr.copy()
        arr3 = arr.copy()

        ans1 = max_top_k1(arr1, k)
        ans2 = max_top_k2(arr2, k)
        ans3 = max_top_k3(arr3, k)
        if not is_equal(ans1, ans2) or not is_equal(ans1, ans2):
            print('出错了')
            print(arr)
            print(ans1)
            print(ans2)
            print(ans3)
            break
    print('测试结束')
