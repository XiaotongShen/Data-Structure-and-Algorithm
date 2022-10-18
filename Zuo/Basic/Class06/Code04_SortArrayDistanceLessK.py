# -*- coding: utf-8 -*-

"""
@File: Code04_SortArrayDistanceLessK.py
@Author: Sarah Shen
@Time: 15/10/2022 16:58
"""
from queue import PriorityQueue


def sorted_arr_distance_less_than_k(arr: list, k: int):
    if k == 0:
        return
    heap = PriorityQueue()
    index = 0
    for i in range(min(len(arr) - 1, k - 1)):
        # print("index is %i." % i)
        heap.put(arr[index])
        index += 1
    i = 0
    while index < len(arr):
        # print("index is %i, i is %i." % (index, i))
        heap.put(arr[index])
        arr[i] = heap.get()
        index += 1
        i += 1
    while not heap.empty():
        # print("i is %i" % i)
        arr[i] = heap.get()
        i += 1


if __name__ == "__main__":
    # q = PriorityQueue()
    # print(q.empty())
    # print(not q.empty())
    # print(q.queue)
    # q.put(2)
    # q.put(3)
    # q.put(1)
    # q.put(6)
    # q.put(4)
    # q.put(5)
    # print(q.queue)
    # print(q.get())
    # print(q.queue)
    # print(q.empty())

    a = [2, 3, 1, 6, 4, 5]
    print("第1次打印：")
    print(a)
    sorted_arr_distance_less_than_k(a, 3)
    print("第2次打印：")
    print(a)



    # 看一下queue这个module
