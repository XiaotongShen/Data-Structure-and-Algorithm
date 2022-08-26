# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/6/30.
Author: 
    Sarah Shen
Date: 
    2022/6/30
"""

print("========== 选择排序 ==========")
def printArray(arr):
    sorted_arr = ""
    for i in range(len(arr)):
        sorted_arr = sorted_arr+" "+str(arr[i])
    print(sorted_arr)


def SelectSort(arr):
    # 先想边界条件, 当数组为空或数组中只有一个元素的时候，不用排序
    # 直接返回原数组
    if arr is None or len(arr) < 2:
        return arr
    n = len(arr)
    for i in range(n):
        minValueIndex = i
        for j in range(i+1, n):
            if arr[j] < arr[minValueIndex]:
                minValueIndex = j
            else:
                pass
        swap(arr, i, minValueIndex)
    return arr

def swap(arr, i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp


a = [7,1,3,5,1,6,8,1,3,5,7,5]
b = []
c = [9]
d = [5,3,7,9,2,0,8,5,11,2,5,22,34]

printArray(a)
printArray(SelectSort(a))

printArray(b)
printArray(SelectSort(b))

printArray(c)
printArray(SelectSort(c))

printArray(d)
printArray(SelectSort(d))

print("========== 冒泡排序 ==========")


