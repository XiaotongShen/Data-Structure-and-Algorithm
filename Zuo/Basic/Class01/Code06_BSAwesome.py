# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/26.
Author: 
    Sarah Shen
Date: 
    2022/8/26
"""
import random


class Test:
    """ 排序算法的对数器，随机生成数组，比较两个不同的算法结果是否一致 """
    def main(self, times: int, max_len: int, max_val: int, func):
        succeed = True
        for i in range(times):
            arr = self.generate_random_array(max_len, max_val)
            ans1 = func(arr)
            ans2 = self.comparator(arr, ans1)
            if ans1 != ans2:
                succeed = False
                print(arr)
                print(ans1, ans2)
                break
        print("Nice!" if succeed else "Oops, Something is Wrong!")

    @staticmethod
    def generate_random_array(max_len, max_val):
        """ 生成相邻不相等的数组 """
        cur_len = int(random.random()*max_len)
        arr = list()
        arr.append(int(random.random() * max_val))
        cur = int(random.random() * max_val)
        for i in range(1, cur_len):
            while cur == arr[i-1]:
                cur = int(random.random() * max_val)
            arr.append(cur)
        return arr

    @staticmethod
    def comparator(arr: list, index: int):
        ans = -1
        if arr is None or len(arr) < 1:
            return ans
        elif index == 0 and len(arr) == 1:
            ans = index
            return ans
        elif index == 0 and arr[index] < arr[index + 1]:
            ans = index
            return ans
        elif index == len(arr) - 1 and arr[index] < arr[index - 1]:
            ans = index
            return ans
        else:
            ans = index if arr[index] < arr[index - 1] and arr[index] < arr[index + 1] else -1
            return ans


def get_local_minimum_index(arr: list):
    if arr is None or len(arr) < 1:
        return -1
    elif len(arr) == 1 or (len(arr) > 1 and arr[0] < arr[1]):
        return 0
    elif arr[len(arr)-1] < arr[len(arr) - 2]:
        return len(arr)-1
    else:
        left = 1
        right = len(arr) - 2
        while left < right:
            mid = left + ((right - left) >> 1)
            if arr[mid] > arr[mid+1]:
                left = mid + 1
            elif arr[mid] > arr[mid - 1]:
                right = mid - 1
            else:
                return mid
        return left


if __name__ == '__main__':

    test = Test()
    test.main(times=100000, max_len=20, max_val=20, func=get_local_minimum_index)
