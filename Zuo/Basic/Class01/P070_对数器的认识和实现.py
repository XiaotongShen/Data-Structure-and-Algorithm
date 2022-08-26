# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/25.
Author: 
    Sarah Shen
Date: 
    2022/8/25
"""


# 写好了算法过程，找不到测试用例，大样本出错，你好心烦。。。这个时候可用对数器
#
# 同样一个功能，可以用多种方式去实现，差的办法总能写出来的，我们往往想测的是自认为相当好的办法的正确与否
#
# 有两个方法A，B，不考虑谁更优，是两套思路下的办法，如果随机产生了数据很多大样本，如果两个方法的结果是一样的，就可以说明大概率下，两个方法都是对的，这个想法有点绝，符合概率论的观点。
# 生成随机样本，测试两个方法结果是否一直。可以不依赖别人提供的测试用例， 竞赛的朋友们都是用这个方法来联系code的


import random


class IsRightSortMethod:
    """ 构造排序算法的对数器 """

    def generate_random_arr(self, max_len: int, max_val: int):
        """ 生成一个最大长度max_len， 最大值是max_val的随机数组 """
        cur_len = int(random.random()*max_len)
        arr = []
        for i in range(cur_len):
            arr.append(int(random.random()*max_val))
        return arr

    def right_method(self, arr: list):
        arr.sort()
        return arr

    def is_right(self, test_times: int, max_len: int, max_val: int, func):
        """
        随机生成test_time个随机数组（test_times个样本数据），每个随机数组（样本）的最大长度为max_len，最大值为max_val
        判断在这些样本下func的结果与right_method结果是否一直，
        如果全部通过，则说明方法是对的，通过了测试
        """
        success = True
        for i in range(test_times):
            arr = self.generate_random_arr(max_len, max_val)
            arr1 = arr.copy()
            arr2 = arr1.copy()
            self.right_method(arr1)
            func(arr2)
            if arr1 != arr2:
                success = False
                print(arr)
                break
        print('Nice!' if success else 'Oops, Something Went Wrong!')


class InsertSort:
    """ 构造插入排序的算法过程 """
    def insert_sort(self, arr: list):
        if arr is None or len(arr) < 2:
            return arr
        else:
            for i in range(1, len(arr)):
                # print('i is %i' % i)
                for j in range(i, 0, -1):
                    # print(j-1, j)
                    if arr[j] <= arr[j - 1]:
                        self.swap(arr, j, j - 1)
                    else:
                        pass
            return arr

    def swap(self, arr: list, a: int, b: int):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp


if __name__ == '__main__':
    Is = InsertSort()
    right_sort = IsRightSortMethod()

    right_sort.is_right(50000, 100, 100, Is.insert_sort)
