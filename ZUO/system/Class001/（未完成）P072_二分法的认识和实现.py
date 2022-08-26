# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/25.
Author: 
    Sarah Shen
Date: 
    2022/8/25
"""

# 最经典的使用二分法解决的问题，在一个有序数组中找某个数存在与否
#   如果用遍历的方法来处理，时间复杂度是O(N)
#   更好的办法，使用二分法 O(logN), 一次砍一半，一次砍一半。。。

# 有序不是所有问题使用二分法的必要条件， 只要能正确构建左右两侧的淘汰逻辑，就可以使用二分法

# 体会以下可以使用二分法的例子
#   eg1. 在有序数组中，判断某个数是否存在
#   eg2. 在有序数组中，找到>=某个数最左的位置
#   eg3. 在有序数组中，找到<=某个数最右的位置
#   eg4. 局部最小值问题


def exist(arr: list, num: int):
    """ 在有序数组arr中，判断数num是否存在 """
    if arr is None or len(arr) < 1:
        return False
    else:
        li = 0
        ri = len(arr) - 1
        while li < ri:
            mid = li + ((ri - li) >> 1)
            if arr[mid] == num:
                return True
            elif arr[mid] > num:
                ri = mid - 1
            else:
                li = mid + 1
        return arr[li] == num   # 如果不符合while的条件，仅剩的情况为li == ri, 即数组中只有一个位置伤的数需要判断，那么只需要判断这一个位置上的数是否等于num，返回结果即好


def get_one_local_min(arr: list):
    """ 局部最小值问题, 获取数组中的一个局部最小值 """
    if arr is None or len(arr) < 1:
        return None
    elif len(arr) == 1:
        return arr[0]
    else:
        pass
