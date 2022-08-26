# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/3/11.
Author: 
    Sarah Shen
Date: 
    2022/3/11
"""

# 分而治之 - divide and conquer, D&C
# (1) 找出基线条件
# (2) 不断将问题分解，直到符合基线条件
# 寻找两个数的最大公约数的算法

# 使用循环计算和
a = [1,2,3,4]
def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total
# print(sum(a))


# 使用递归计算和
def sum_r(arr):
    total = 0
    # 基线条件
    if arr == []:
        return 0
    elif len(arr) == 1:
        return arr[0]
    # 递归条件
    else:
        total = arr[0] + sum(arr[1:])
    return total

# print(sum_r(a))

# print(a[0], a[1:], len(a))



# 使用递归找出列表中最大的数
def max_num(arr):
    if arr == []:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        if arr[0] >= max_num(arr[1:]):
            return arr[0]
        else:
            return max_num(arr[1:])

# print(max_num(a))

b = [10, 5, 2, 3]

# 使用递归进行快速排序
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort(b))
