# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/6/30.
Author: 
    Sarah Shen
Date: 
    2022/6/30
"""

def PreSum(arr, end):
    n = len(arr)
    print()
    if end < 0:
        end = 0
    elif end > n-1:
        end = n-1
    else:
        end = end
    presum = 0
    for i in range(end+1):
        v = arr[i]
        presum += v
    return presum



def RangeSum(arr, l, r):
    if l < r:
        rangesum = 0
    else:
        rangesum = PreSum(arr, r) - PreSum(arr, l-1)
    return rangesum



a = [1,2,3,4,5,6,7,8,9]
n = len(a)
print(a)
for i in range(n):
    print(i, a[i])

for i in range(-5, 20):
    print(i, PreSum(a, i))

print(RangeSum(a, 9,10))





