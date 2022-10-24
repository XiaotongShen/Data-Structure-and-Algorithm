# -*- coding: utf-8 -*-

"""
@File: Code02_LessMoneySplitGold.py
@Author: Sarah Shen
@Time: 23/10/2022 00:25
"""
import sys
from queue import PriorityQueue


# 暴力递归方法
def less_money1(arr):
    if arr is None or len(arr) == 0:
        return 0
    return process(arr, 0)


# 等待合并的数都在arr里，pre之前的合并行为产生了多少总代价
# arr中只剩一个数字的时候，停止合并，返回最小的总代价
def process(arr, pre):
    if len(arr) == 1:
        return pre
    ans = sys.maxsize
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            ans = min(ans, process(copy_and_merge_two(arr, i, j), pre + arr[i] + arr[j]))
        return ans


def copy_and_merge_two(arr, i: int, j: int):
    ans = [None] * (len(arr) - 1)
    ansi = 0
    for arri in range(len(arr)):
        if arri != i and arri != j:
            ans[ansi] = arr[arri]
            ansi += 1
    ans[ansi] = arr[i] + arr[j]
    return ans


# 贪心策略：哈夫曼编码
def less_money2(arr):
    # 利用小根堆，将数组放入小根堆
    pq = PriorityQueue()
    for i in range(len(arr)):
        pq.put(arr[i])
    total_money = 0
    while pq.qsize() > 1:
        cur = pq.get() + pq.get()
        total_money += cur
        pq.put(cur)
    return total_money


if __name__ == '__main__':
    a = [2, 1, 7, 3, 4, 2, 1]
    print(less_money1(a))
    print()
    print(less_money2(a))
