# -*- coding: utf-8 -*-

"""
@File: Code01_MonotonousStack.py
@Author: Sarah Shen
@Time: 31/10/2022 22:46
"""
import random


def get_near_less_no_repeat(arr: [int]):
    res = [[0] * 2 for i in range(len(arr))]
    # 只保存位置
    stack = list()
    for i in range(len(arr)):  # 遍历到i位置的数，arr[i]
        while len(stack) != 0 and arr[stack[-1]] > arr[i]:
            j = stack.pop()
            left_less_index = -1 if len(stack) == 0 else stack[-1]
            res[j][0] = left_less_index
            res[j][1] = i
        stack.append(i)
    while len(stack) != 0:
        j = stack.pop()
        left_less_index = -1 if len(stack) == 0 else stack[-1]
        res[j][0] = left_less_index
        res[j][1] = -1
    return res


def get_near_less(arr: [int]):
    res = [[0] * 2 for i in range(len(arr))]
    s = list()
    for i in range(len(arr)):
        while len(s) != 0 and arr[s[-1][0]] > arr[i]:
            j_groups = s.pop()
            left_less_index = -1 if len(s) == 0 else s[-1][-1]
            for j in j_groups:
                res[j][0] = left_less_index
                res[j][1] = i
        if len(s) != 0 and arr[s[-1][0]] == arr[i]:
            s[-1].append(i)
        else:
            new_group = list()
            new_group.append(i)
            s.append(new_group)
    while len(s) != 0:
        j_groups = s.pop()
        left_less_index = -1 if len(s) == 0 else s[-1][-1]
        for j in j_groups:
            res[j][0] = left_less_index
            res[j][1] = -1
    return res


def get_random_array_no_repeat(size: int):
    arr = [0] * int(random.random() * size + 1)
    for i in range(len(arr)):
        arr[i] = i
    for i in range(len(arr)):
        swap_index = int(random.random() * len(arr))
        tmp = arr[swap_index]
        arr[swap_index] = arr[i]
        arr[i] = tmp
    return arr


def get_random_array(size: int, max_v: int):
    arr = [0] * int(random.random() * size + 1)
    for i in range(len(arr)):
        arr[i] = int(random.random() * max_v) - int(random.random() * max_v)
    return arr


def right_way(arr: [int]):
    """ 测试用的正确的方法 """
    res = [[0] * 2 for i in range(len(arr))]
    for i in range(len(arr)):
        left_less_index = -1
        right_less_index = -1
        cur = i - 1
        while cur >= 0:
            if arr[cur] < arr[i]:
                left_less_index = cur
                break
            cur -= 1
        cur = i + 1
        while cur < len(arr):
            if arr[cur] < arr[i]:
                right_less_index = cur
                break
            cur += 1
        res[i][0] = left_less_index
        res[i][1] = right_less_index
    return res


def is_equal(res1, res2):
    if len(res1) != len(res2):
        return False
    for i in range(len(res1)):
        if res1[i][0] != res2[i][0] or res1[i][1] != res2[i][1]:
            return False
    return True


if __name__ == '__main__':
    size = 10
    max_values = 20
    test_times = 200000
    print('测试开始')
    for i in range(test_times):
        arr1 = get_random_array_no_repeat(size)
        arr2 = get_random_array(size, max_values)
        ans1 = right_way(arr1)
        ans2 = get_near_less_no_repeat(arr1)
        ans3 = right_way(arr2)
        ans4 = get_near_less(arr2)
        if not is_equal(ans1, ans2):
            print('Oops!')
            print(arr1)
            print(ans1)
            print(ans2)
            break
        if not is_equal(ans3, ans4):
            print('Oops!')
            print(arr2)
            print(ans3)
            print(ans4)
            break
    print('测试结束')
