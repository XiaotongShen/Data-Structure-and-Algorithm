# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/7/1.
Author: 
    Sarah Shen
Date: 
    2022/7/1
"""

import random


# ========== 生成随机数组 ========== #
def generateRandomArray(maxlen, maxvalue):
    len = int(random.random()*maxlen)
    arr = [0]*len
    for i in range(len):
        arr[i] = int(random.random()*maxvalue)
    return arr



# ========== 在有序数组中找到大于等于num的最左的位置 ========== #
# # 测试用例
# def test(arr, num):
#     n = len(arr)
#     ans = -1
#     for i in range(n):
#         if arr[i] >= num:
#             ans = i
#             break
#     return ans

# # 测试测试用例
# idx = [0,1,2,3,4,5,6,7,8,9,10]
# arr = [1,2,4,5,6,7,7,8,8,9,10]
# # print(test(arr,8))

# 二分算法
def mostLeftNolessNumIndex(arr, num):
    if arr is None or len(arr) == 0:
        return -1
    L = 0
    R = len(arr) - 1
    ans = -1
    while L <= R:
        # ans更新
        mid = int((L+R)/2)
        if arr[mid] >= num:
            ans = mid
            R = mid - 1
        else:
            L = mid + 1
    return ans

# 对数器 - 生成随机结果对比 二分算法 和 测试用例的结果是否一致
def main():
    testTime = 10000
    maxlen = 10
    maxvalue =100
    success = True
    for i in range(testTime):
        arr = generateRandomArray(maxlen, maxvalue)
        arr.sort()
        value = int((maxvalue + 1) * random.random()) - int(maxvalue * random.random())
        if test(arr, value) != mostLeftNolessNumIndex(arr, value):
            print(arr, value)
            print('出错了！')
            success = False
            break
    if success:
        print("Nice!")
    else:
        print("F...")

# main()


# ========== 在有序数组中找到小于等于num的最右的位置 ========== #
# 测试用例
def test(arr, num):
    n = len(arr)
    ans = -1
    for i in range(n):
        if arr[i] <= num:
            ans = i
    return ans

# # 测试测试用例
# idx = [0,1,2,3,4,5,6,7,8,9,10]
# arr = [1,2,4,5,6,7,7,8,8,9,10]
# print(test(arr,0))


# 二分算法
def mostRightNoMoreNumIndex(arr, num):
    if arr is None or len(arr) == 0:
        return -1
    L = 0
    R = len(arr) - 1
    ans = -1
    while L <= R:
        # ans更新
        mid = int((L+R)/2)
        if arr[mid] <= num:
            ans = mid
            L = mid + 1
        else:
            R = mid - 1
    return ans

# idx = [0,1,2,3,4,5,6,7,8,9,10]
# arr = [1,2,4,5,6,7,7,8,8,9,10]
# print(mostRightNoMoreNumIndex(arr,8))

# 对数器 - 生成随机结果对比 二分算法 和 测试用例的结果是否一致
def main():
    testTime = 10000
    maxlen = 10
    maxvalue =100
    success = True
    for i in range(testTime):
        arr = generateRandomArray(maxlen, maxvalue)
        arr.sort()
        value = int((maxvalue + 1) * random.random()) - int(maxvalue * random.random())
        if test(arr, value) != mostRightNoMoreNumIndex(arr, value):
            print(arr, value)
            print('出错了！')
            success = False
            break
    if success:
        print("Nice!")
    else:
        print("F...")

main()


