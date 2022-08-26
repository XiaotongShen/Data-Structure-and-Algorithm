# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/25.
Author: 
    Sarah Shen
Date: 
    2022/8/25
"""

# 插入排序，时间复杂度（N*N) = O(N^2)
# 0～0有序：0有序
# 0～1有序：0-1有序
# 0～2有序：1-2有序，0-1有序
# 0～3有序：2-3有序，1-2有序， 0-1有序
# ...
# 0～n-1有序：(n-2)-(n-1)有序, ..., 0-1有序

# Note: 流程的状况会随数据的状况而变化，因此流程的时间复杂度是流程随数据情况变化的最差情况，这里插入排序的最好情况是O(N), 最差情况O(N^2)


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
