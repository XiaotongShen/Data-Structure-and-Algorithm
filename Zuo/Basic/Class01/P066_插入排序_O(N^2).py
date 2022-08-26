# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/25.
Author: 
    Sarah Shen
Date: 
    2022/8/25
"""




def insert_sort(arr:list):
    if arr is None or len(arr) < 2:
        return arr
    else:
        for i in range(1, len(arr)):
            # print('i is %i' % i)
            for j in range(i, 0, -1):
                # print(j-1, j)
                if arr[j] <= arr[j-1]:
                    swap(arr, j, j-1)
                else:
                    pass
        return arr


def swap(arr: list, a: int, b: int):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


if __name__ == '__main__':

    a = [3, 2, 3, 1, 4, 0]

    print(insert_sort(a))
