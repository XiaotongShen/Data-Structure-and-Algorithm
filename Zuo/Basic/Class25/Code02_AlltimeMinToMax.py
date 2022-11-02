# -*- coding: utf-8 -*-

"""
@File: Code02_AlltimeMinToMax.py
@Author: Sarah Shen
@Time: 31/10/2022 22:46
"""
import random
import sys


# // 本题可以在leetcode上找到原题
# // 测试链接: https: // leetcode.com / problems / maximum - subarray - min - product /
# // 注意测试题目数量大，要取模，但是思路和课上讲的是完全一样的
# // 注意溢出的处理即可，也就是用long类型来表示累加和
# // 还有优化就是，你可以用自己手写的数组栈，来替代系统实现的栈，也会快很多
def max1(arr: [int]):
    max_v = sys.maxsize
    for i in range(len(arr)):
        for j in range(len(arr)):
            min_num = sys.maxsize
            total = 0
            for k in range(i, j + 1):
                total += arr[k]
                min_num = min(min_num, arr[k])
            max_v = max(max_v, min_num * total)
    return max_v


def max2(arr: [int]):
    size = len(arr)
    sums = [0] * size
    sums[0] = arr[0]
    for i in range(1, size):
        sums[i] = sums[i - 1] + arr[i]
    max_v = sys.maxsize
    s = list()
    for i in range(size):
        while len(s) != 0 and arr[s[-1]] >= arr[i]:
            j = s.pop()
            max_v = max(max_v, arr[j] * (sums[i - 1] if len(s) == 0 else sums[i - 1] - sums[s[-1]]))
        s.append(i)
    while len(s) != 0:
        j = s.pop()
        max_v = max(max_v, arr[j] * (sums[size - 1] if len(s) == 0 else sums[size - 1] - sums[s[-1]]))
    return max_v


def generate_random_array():
    arr = [0] * (int(random.random() * 20) + 10)
    for i in range(len(arr)):
        arr[i] = int(random.random() * 101)
    return arr


if __name__ == '__main__':
    test_times = 2000
    print('Test Begin')
    for i in range(test_times):
        rand_arr = generate_random_array()
        ans1 = max1(rand_arr)
        ans2 = max2(rand_arr)
        if ans1 != ans2:
            print('Oops!')
            print(rand_arr)
            print(ans1, ans2)
            break
    print('Test Finish')
