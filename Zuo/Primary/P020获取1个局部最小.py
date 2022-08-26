# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/7/1.
Author: 
    Sarah Shen
Date: 
    2022/7/1
"""

# 整体无序，且相邻位置不相等
# ========== 二分法，找到无序，相邻元素不相等的数组中的一个局部最小 ========== #
# 局部最小，小于所有相邻元素
#
def oneMinIndex(arr):
    # 首先考虑边界条件
    if arr is None or len(arr) == 0:
        return -1
    if len(arr) == 1:
        return 0
    N = len(arr)
    if arr[0] < arr[1]:
        return 0
    if arr[N-1] < arr[N-2]:
        return N-1
    L = 0
    R = N-1
    ans = -1
    while L <= R:
        mid = int((L+R)/2)
        if (arr[mid - 1] > arr[mid]) and (arr[mid] < arr[mid+1]):
            ans = mid
            break
        elif arr[mid] > arr[mid-1]:
            R = mid -1
        else:
            L = mid + 1
    return ans


# ========== 生成随机数组，且相邻数不相等 ========== #
import random
def generateRandomArray(maxlen, maxvalue):
    len = int(random.random()*maxlen)
    arr = [0]*len
    if len > 0:
        arr[0] = int(random.random() * maxvalue)
        for i in range(1,len):
            arr[i] = int(random.random() * maxvalue)
            while (arr[i-1] == arr[i]):
                arr[i] = int(random.random() * maxvalue)
    return arr

# print(generateRandomArray(50, 5))

# ========== 生成测试函数 ========== #
def check(arr, minIndex):
    if len(arr) == 0:
        return minIndex == -1
    left = minIndex - 1
    right = minIndex + 1
    if left >= 0:
        leftBigger = (arr[left] > arr[minIndex])
    else:
        leftBigger = True
    if right <= len(arr) - 1:
        rightBigger = (arr[right] > arr[minIndex])
    else:
        rightBigger = True
    return (leftBigger and rightBigger)

# 对数器 - 生成随机结果对比 二分算法 和 测试用例的结果是否一致
def main():
    testTime = 10000
    maxlen = 10
    maxvalue =100
    success = True
    for i in range(testTime):
        arr = generateRandomArray(maxlen, maxvalue)
        arr.sort()
        inx = oneMinIndex(arr)
        if check(arr, inx) is False:
            print(arr, inx)
            print('出错了！')
            success = False
            break
    if success:
        print("Nice!")
    else:
        print("F...")

main()

# a = generateRandomArray(10, 5)
# print(a)
# a = [4, 3, 2, 3, 4, 0, 1, 4]
# print(check(a, 2))
# print(check(a, 4))






