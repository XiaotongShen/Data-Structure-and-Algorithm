# -*- coding: utf-8 -*-

"""
@File: Code01_SumOfSubarrayMinimums.py
@Author: Sarah Shen
@Time: 02/11/2022 17:37
"""
import random


# 测试链接：https://leetcode.com/problems/sum-of-subarray-minimums/
# subArrayMinSum1是暴力解
# subArrayMinSum2是最优解的思路
# sumSubarrayMin是最优解思路下的单调栈优化
# Leetcode上不要提交subArrayMinSum1、subArrayMinSum2方法，因为没有考虑取摸
# Leetcode上只提交sumSubarrayMin方法，时间复杂度O(N)，可以直接通过
def sum_array_min_sum1(arr: [int]):
    ans = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            min_value = arr[i]
            for k in range(i + 1, j + 1):
                min_value = min(min_value, arr[k])
            ans += min_value
    return ans


def sub_array_min_sum2(arr: [int]):
    # left[i] = x: arr[i]左边，离arr[i]最近，<=arr[i],位置在x
    left = left_near_less_equal2(arr)
    # right[i] =y: arr[i]右边，离arr[i]最近，< arr[i],位置在y
    right = right_near_less2(arr)
    ans = 0
    for i in range(len(arr)):
        start = i - left[i]
        end = right[i] - i
        ans += start * end * arr[i]
    return ans


def left_near_less_equal2(arr: [int]):
    n = len(arr)
    left = [0] * n
    for i in range(n):
        ans = -1
        for j in range(i - 1, -1, -1):
            if arr[j] <= arr[i]:
                ans = j
                break
        left[i] = ans
    return left


def right_near_less2(arr: [int]):
    n = len(arr)
    right = [0] * n
    for i in range(n):
        ans = n
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                ans = j
                break
        right[i] = ans
    return right


def sum_sub_array_min(arr: [int]):
    stack = []
    left = near_less_equal_left(arr, stack)
    right = near_less_right(arr, stack)
    ans = 0
    for i in range(len(arr)):
        start = i - left[i]
        end = right[i] - i
        ans += start * end * arr[i]
        ans %= 1000000007
    return ans


def near_less_equal_left(arr: [int], stack: [int]):
    n = len(arr)
    left = [0] * n
    for i in range(n - 1, -1, -1):
        while len(stack) != 0 and arr[stack[-1]] >= arr[i]:
            j = stack.pop()
            left[j] = i
        stack.append(i)
    while len(stack) != 0:
        j = stack.pop()
        left[j] = -1
    return left


def near_less_right(arr: [int], stack: [int]):
    n = len(arr)
    right = [0] * n
    for i in range(n):
        while len(stack) != 0 and arr[stack[-1]] > arr[i]:
            j = stack.pop()
            right[j] = i
        stack.append(i)
    while len(stack) != 0:
        j = stack.pop()
        right[j] = n
    return right


class Solution:

    # def sumSubarrayMins(self, arr: List[int]) -> int:
    def sum_sub_array_min(self, arr: [int]):
        stack = []
        left = self.near_less_equal_left(arr, stack)
        right = self.near_less_right(arr, stack)
        ans = 0
        for i in range(len(arr)):
            start = i - left[i]
            end = right[i] - i
            ans += start * end * arr[i]
            ans %= 1000000007
        return ans

    @staticmethod
    def near_less_equal_left(arr: [int], stack: [int]):
        n = len(arr)
        left = [0] * n
        for i in range(n - 1, -1, -1):
            while len(stack) != 0 and arr[stack[-1]] >= arr[i]:
                j = stack.pop()
                left[j] = i
            stack.append(i)
        while len(stack) != 0:
            j = stack.pop()
            left[j] = -1
        return left

    @staticmethod
    def near_less_right(arr: [int], stack: [int]):
        n = len(arr)
        right = [0] * n
        for i in range(n):
            while len(stack) != 0 and arr[stack[-1]] > arr[i]:
                j = stack.pop()
                right[j] = i
            stack.append(i)
        while len(stack) != 0:
            j = stack.pop()
            right[j] = n
        return right


def random_array(max_l: int, max_v: int):
    n = int(random.random() * max_l)
    ans = [0] * n
    for i in range(n):
        ans[i] = int(random.random() * max_v) + 1
    return ans


if __name__ == '__main__':
    max_len = 100
    max_value = 50
    test_times = 1000
    print('测试开始')
    for i in range(test_times):
        r_arr = random_array(max_len, max_value)
        ans1 = sum_array_min_sum1(r_arr)
        ans2 = sub_array_min_sum2(r_arr)
        ans3 = sum_sub_array_min(r_arr)
        if ans1 != ans2 or ans1 != ans3:
            print('Oops!')
            print(r_arr)
            print(ans1, ans2, ans2)
            break
    print('测试结束')

