# -*- coding: utf-8 -*-

"""
Description:

Author: 
    Sarah Shen
Date: 
    2022/7/1
"""

def swap(arr, i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp

# 选择排序
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

# 冒泡排序
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

# 插入排序
def InsertSort(arr):
    # 先想边界条件, 当数组为空或数组中只有一个元素的时候，不用排序
    # 直接返回原数组
    if arr is None or len(arr) < 2:
        return arr
    n = len(arr)
    # 0-0
    # 0-1 0-0
    # 0-2 0-1 0-0
    for i in range(1,n):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                swap(arr, j-1, j)
            else:
                pass
    return arr


import random
# 对数器，用来调bug，生成随机样本自己做比对的机器
# 接下来创建一个对数器，给定一个最大长度和最大值，随机生成一个数组，随机长度和随机值
# 对随机生成的数据组进行排序，验证数组是否是有序的

# 返回一个数组arr， arr长度[0, maxlen), arr中的每个值[0, maxvalue)
def LenRandomValueRandow(maxlen, maxvalue):
    len = int(random.random()*maxlen)
    arr = [0]*len
    for i in range(len):
        arr[i] = int(random.random()*maxvalue)
    return arr


# 检查两个等长的arry是否是一样的, 这个python的数据结构list可以直接实现对比
def EqualArrayValues(arr1, arr2):
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

def isSorted(arr):
    if len(arr) < 2:
        return True
    else:
        max = arr[0]
        for i in range(len(arr)):
            if max > arr[i]:
                return False
            else:
                max = arr[i]
        return True


# arr = [1,2,3,0,5,5,6,7,7,8]
# print(isSorted(arr))
def WrongSelectSort(arr):
    # 先想边界条件, 当数组为空或数组中只有一个元素的时候，不用排序
    # 直接返回原数组
    if arr is None or len(arr) < 2:
        return arr
    n = len(arr)
    for i in range(n):
        minValueIndex = i
        for j in range(i+1, n):
            if arr[j] > arr[minValueIndex]:
                minValueIndex = j
            else:
                pass
        swap(arr, i, minValueIndex)
    return arr



def main():
    maxlen = 5
    maxvalue =1000
    testTime = 10000
    for i in range(testTime):
        arr1 = LenRandomValueRandow(maxlen, maxvalue)
        temp = arr1.copy()
        if isSorted(SelectSort(arr1)) is not True:
            print(temp)
            print(WrongSelectSort(arr1))
            print(SelectSort(arr1))
            print("选择排序错了！")
            break
# main()





list_old = [3]*5
list_assign  = list_old
list_copy = list_old.copy()

print(list_old, id(list_old), "(list)")
print(list_assign, id(list_assign), "(assign)")
print(list_copy, id(list_copy), "(copy)")













