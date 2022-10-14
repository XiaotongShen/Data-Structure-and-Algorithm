# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/29.
Author: 
    Sarah Shen
Date: 
    2022/8/29
"""

if __name__ == '__main__':
    a = 102
    b = 10

    print(a, b)
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(a, b)

    arr = [100, 89, 77, 23, 4, 5, 7, 1, 19]
    i = 3
    j = 5

    print(arr[i], arr[j])
    arr[i] = arr[i] ^ arr[j]
    arr[j] = arr[i] ^ arr[j]
    arr[i] = arr[i] ^ arr[j]
    print(arr[i], arr[j])
