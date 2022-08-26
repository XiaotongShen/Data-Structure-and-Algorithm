# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/6/30.
Author: 
    Sarah Shen
Date: 
    2022/6/30
"""

def swap(arr, i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp

def printArray(arr):
    sorted_arr = ""
    for i in range(len(arr)):
        sorted_arr = sorted_arr+" "+str(arr[i])
    print(sorted_arr)

def BubbleSort(arr):
    # 先想边界条件, 当数组为空或数组中只有一个元素的时候，不用排序
    # 直接返回原数组
    if arr is None or len(arr) < 2:
        return arr
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range(i):
            first = arr[j]
            second = arr[j+1]
            if first > second:
                swap(arr, j, j+1)
            else:
                pass
    return arr

b = []
c = [9]
a = [7,1,3,5,1,6,8,1,3,5,7,5]
d = [5,3,7,9,2,0,8,5,11,2,5,25,3]

printArray(a)
printArray(BubbleSort(a))

printArray(b)
printArray(BubbleSort(b))

printArray(c)
printArray(BubbleSort(c))

printArray(d)
printArray(BubbleSort(d))