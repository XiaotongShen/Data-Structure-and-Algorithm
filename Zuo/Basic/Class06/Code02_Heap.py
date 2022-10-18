# -*- coding: utf-8 -*-

"""
@File: Code02_Heap.py
@Author: Sarah Shen
@Time: 15/10/2022 16:58
"""


class MyMaxHeap:
    """ 用列表定义一个大跟堆 """
    def __init__(self, limit):
        self.limit = limit
        self.heap = [0] * limit
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.limit

    def push(self, value: int):
        if self.size == self.limit:
            print("Heap is full!")
            return
        self.heap[self.size] = value
        self.heap_insert(self.heap, self.size)
        self.size += 1

    def pop(self):
        ans = self.heap[0]
        self.swap(self.heap, 0, max(0, self.size - 1))
        if self.size != 0:
            self.size -= 1
        self.heapify(self.heap, 0, self.size)
        return ans

    def heap_insert(self, arr: list, index: int):
        # 新加进来的书，现在停在了index位置，请依次往上移动
        # 移动到0位置，或者PK不掉自己的父节点，停！
        while (arr[index]) > arr[int((index - 1) / 2)]:
            self.swap(arr, index, int((index - 1) / 2))
            index = int((index - 1) / 2)

    def heapify(self, arr: [int], index: int, size: int):
        left = index * 2 + 1
        while left < size:
            # 当前节点在index位置，其子节点的位置为index*2+1
            # 有左节点的情况下，右节点可能有可能没有
            largest = left + 1 if (left + 1 < size) and (arr[left + 1] > arr[left]) else left
            largest = largest if arr[largest] > arr[index] else index
            if largest == index:
                break
            self.swap(arr, largest, index)
            index = largest
            left = index * 2 + 1

    @staticmethod
    def swap(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


class RightMaxHeap:
    """ 暴力的方式方式实现一个大根堆"""
    def __init__(self, limit):
        self.heap = [0] * limit
        self.limit = limit
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.limit

    def push(self, value):
        if self.size == self.limit:
            print("Heap is full!")
            return
        self.heap[self.size] = value
        self.size += 1

    def pop(self):
        if self.size == 0:
            print("Heap is empty!")
            return
        else:
            max_index = 0
            for i in range(self.size):
                if self.heap[i] > self.heap[max_index]:
                    max_index = i
            ans = self.heap[max_index]
            self.heap[max_index] = self.heap[self.size - 1]
            if self.size != 0:
                self.size -= 1
            return ans


def my_comparator(o1: int, o2: int):
    return o2 - o1


if __name__ == "__main__":
    print("第1次打印")
    # hp = MyMaxHeap(5)
    hp = RightMaxHeap(5)
    print(hp.heap)
    print(hp.size)

    print("第2次打印")
    hp.push(1)
    print(hp.heap)
    print(hp.size)

    print("第3次打印")
    hp.push(2)
    print(hp.heap)
    print(hp.size)

    print("第4次打印")
    hp.push(3)
    print(hp.heap)
    print(hp.size)

    print("第5次打印")
    hp.push(4)
    print(hp.heap)
    print(hp.size)

    print("第6次打印")
    hp.push(5)
    print(hp.heap)
    print(hp.size)

    hp.push(6)
    print("\n")
    print("第1次弹出")
    print(hp.heap)
    print(hp.pop())
    print(hp.size)

    print("第2次弹出")
    print(hp.heap)
    print(hp.pop())
    print(hp.size)

    print("第3次弹出")
    print(hp.heap)
    print(hp.pop())
    print(hp.size)

    print("第4次弹出")
    print(hp.heap)
    print(hp.pop())
    print(hp.size)

    print("第5次弹出")
    print(hp.heap)
    print(hp.pop())
    print(hp.size)
    print(hp.is_empty())

    print("第6次弹出")
    print(hp.heap)
    print(hp.pop())
    print(hp.size)

    print("第7次弹出")
    print(hp.heap)
    print(hp.pop())
    print(hp.size)

