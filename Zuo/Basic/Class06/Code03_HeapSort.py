# -*- coding: utf-8 -*-

"""
@File: Code03_HeapSort.py
@Author: Sarah Shengit
@Time: 15/10/2022 16:58
"""


class HeapSort:

    def heap_sort(self, arr: list):
        # 堆排序额外空间复杂度O(1)
        if arr is None or len(arr) < 2:
            return

        # 数组->堆，方式一
        # for i in range(len(arr)):
        #     self.heapify(arr, i)  # O(logN)
        # 数组->堆，方式二
        # 把原数组看成一个非有效的堆， 从最后一个节点开始向上调整堆的有效性
        for i in range(len(arr) - 1, -1, -1):
            self.heapify(arr, i, len(arr))
        # 调整之后，数组被调成一个有效的大跟堆
        # 依次将堆顶的数调整到最后一个叶节点，然后让堆的size - 1可得到升序的数组
        heap_size = len(arr)
        self.swap(arr, 0, heap_size - 1)
        heap_size -= 1
        while heap_size > 0:
            self.heapify(arr, 0, heap_size)
            self.swap(arr, 0, heap_size - 1)
            heap_size -= 1

    def heap_insert(self, arr: list, index: int):
        while arr[index] > arr[int((index - 1) / 2)]:
            self.swap(arr, index, int((index - 1) / 2))
            index = int((index - 1) / 2)

    def heapify(self, arr: list, index: int, heap_size: int):
        left = index * 2 + 1    # 左侧子节点的下标
        while left < heap_size:
            # 下方还有子节点的时候
            largest = left + 1 if (left + 1 < heap_size) and (arr[left + 1] > arr[left]) else left
            largest = largest if arr[largest] > arr[index] else index
            if largest == index:
                break
            self.swap(arr, largest, index)
            index = largest
            left = index * 2 + 1

    @staticmethod
    def swap(arr: list, i: int, j: int):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


if __name__ == "__main__":
    a = [7, 3, 5, 13, 8, 9, 0, 13]
    print("第1次打印：")
    print(a)
    hs = HeapSort()
    hs.heap_sort(a)
    print("第2次打印：")
    print(a)
