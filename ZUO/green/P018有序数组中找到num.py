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

a = list(range(1, 11))
# print(a)

# 简单的有序二分查找
# arr保证有序
def find(arr, num):
    # 边界条件
    if arr is None and arr.length == 0:
        return False
    L = 0
    R = len(arr) -1
    while(L <= R):
        mid = int((L+R)/2)
        if arr[mid] == num:
            return True
        elif arr[mid] < num:
            L = mid + 1
        else:
            R = mid - 1
    return False

# print(find(a, 0))


def WrongFind(arr, num):
    # 边界条件
    if arr is None and arr.length == 0:
        return False
    L = 0
    R = len(arr) -1
    while(L ==R):
        mid = int((L+R)/2)
        if arr[mid] == num:
            return True
        elif arr[mid] < num:
            L = mid + 1
        else:
            R = mid - 1
    return False

# print(WrongFind(a, 13))

# 最简单的肯定对的查找
def test(sortedArry, num):
    for x in sortedArry:
        if x == num:
            return True
    return False

# 返回一个数组arr， arr长度[0, maxlen), arr中的每个值[0, maxvalue)
def generateRandomArray(maxlen, maxvalue):
    len = int(random.random()*maxlen)
    arr = [0]*len
    for i in range(len):
        arr[i] = int(random.random()*maxvalue)
    return arr

# 生成随机数组来测试两个方法的结果每次都一样
def main():
    testTime = 10000
    maxlen = 10
    maxvalue =100
    success = True
    for i in range(testTime):
        arr = generateRandomArray(maxlen, maxvalue)
        arr.sort()
        value = int((maxvalue + 1) * random.random()) - int(maxvalue * random.random())
        # if test(arr, value) != WrongFind(arr, value):
        if test(arr, value) != find(arr, value):
            print(arr, value)
            print('出错了！')
            success = False
            break
    if success:
        print("Nice!")
    else:
        print("F...")

main()

# b = [3,6,5,1,2,4]
# b.sort()
# c = list(range(0,6))
# # print(b, c)
# print(b != c)

# print(int(random.random() * 100))
# print(int(random.random() * 101))
