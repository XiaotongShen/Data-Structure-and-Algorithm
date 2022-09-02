# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/9/1.
Author:
    Sarah Shen
Date:
    2022/9/1
"""
import random


class QuickSortRecursiveAndNotRecursive:

    @staticmethod
    def swap(arr: list, i: int, j: int):
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp

    def netherlands_flag(self, arr: list, left: int, right: int):
        if left > right:
            return [-1, -1]
        elif left == right:
            return [left, right]
        else:
            less = left - 1
            more = right
            i = left
            while i < more:
                if arr[i] == arr[right]:
                    i += 1
                elif arr[i] < arr[right]:
                    less += 1
                    self.swap(arr, i, less)
                    i += 1
                else:
                    more -= 1
                    self.swap(arr, i, more)
            self.swap(arr, more, right)

            return [less + 1, more]

    def quick_sort_1(self, arr: list):
        """ 快排递归版本 """
        if arr is None or len(arr) < 2:
            return
        else:
            self.process(arr, 0, len(arr) - 1)

    def process(self, arr: list, left: int, right: int):
        if left >= right:
            return
        else:
            self.swap(arr, left + int(random.random() * (right - left + 1)), right)
            equal_area = self.netherlands_flag(arr, left, right)
            self.process(arr, left, equal_area[0] - 1)
            self.process(arr, equal_area[1] + 1, right)

    def quick_sort_2(self, arr: list):
        """ 非递归版本，用栈来执行 """
        if arr is None or len(arr) < 2:
            return
        else:
            n = len(arr)
            self.swap(arr, int(random.random() * n), n - 1)
            equal_area = self.netherlands_flag(arr, 0, n - 1)
            el = equal_area[0]
            er = equal_area[1]
            stack = Stack(items=[])
            stack.push(Op(left=0, right=el - 1))
            stack.push(Op(left=er + 1, right=n - 1))
            while not stack.is_empty():
                op = stack.pop()
                if op.left < op.right:
                    self.swap(arr, op.left + int(random.random() * (op.right - op.left + 1)), op.right)
                    equal_area = self.netherlands_flag(arr, op.left, op.right)
                    el = equal_area[0]
                    er = equal_area[1]
                    stack.push(Op(left=op.left, right=el - 1))
                    stack.push(Op(left=er + 1, right=op.right))

    def quick_sort_3(self, arr: list):
        """ 非递归版本，用队列来执行 """
        if arr is None or len(arr) < 2:
            return
        else:
            n = len(arr)
            self.swap(arr, int(random.random() * n), n - 1)
            equal_area = self.netherlands_flag(arr, 0, n - 1)
            el = equal_area[0]
            er = equal_area[1]
            queue = list()
            queue.append(Op(0, el - 1))
            queue.append(Op(er + 1, n - 1))
            while not len(queue) == 0:
                op = queue.pop()
                if op.left < op.right:
                    self.swap(arr, op.left + int(random.random() * (op.right - op.left + 1)), op.right)
                    equal_area = self.netherlands_flag(arr, op.left, op.right)
                    el = equal_area[0]
                    er = equal_area[1]
                    queue.append(Op(op.left, el - 1))
                    queue.append(Op(er + 1, op.right))


class Stack:
    """ 定义栈 """

    def __init__(self, items=None):
        self.items = items

    def is_empty(self):
        return len(self.items) == 0

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if self.is_empty():
            print("Your Stack is Empty!")
        else:
            num = self.items.pop()
            return num

    def peek(self):
        if self.is_empty():
            print("Your Stack is Empty!")
        else:
            num = self.items[len(self.items) - 1]
            print(num)

    def travel(self):
        print(self.items)


class Queue:
    """ 定义队列 """

    def __init__(self, items=None):
        self.items = items

    def is_empty(self):
        return len(self.items) == 0

    def offer(self, val):
        self.items.append(val)

    def poll(self):
        if self.is_empty():
            print("Your Stack is Empty!")
        else:
            num = self.items[0]
            self.items = self.items[1:]
            return num

    def peek(self):
        if self.is_empty():
            print("Your Stack is Empty!")
        else:
            num = self.items[0]
            print(num)

    def travel(self):
        print(self.items)


class Op:
    """ 快排非递归版本需要的辅助类，要处理什么范围上的排序 """

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


class Test:
    """ 对数器待完成 """

    @staticmethod
    def generate_random_arr(max_len, max_val):
        cur_len = int(random.random() * max_len)
        arr = []
        for i in range(cur_len):
            arr.append(int(random.random() * max_val))
        return arr


if __name__ == '__main__':
    t = Test()
    arr1 = t.generate_random_arr(max_len=20, max_val=20)
    arr2 = arr1.copy()
    arr3 = arr1.copy()

    s = QuickSortRecursiveAndNotRecursive()
    print("====================")
    print(arr1)
    s.quick_sort_1(arr1)
    print(arr1)

    print("====================")
    print(arr2)
    s.quick_sort_2(arr2)
    print(arr2)
    print(arr1 == arr2)

    print("====================")
    print(arr3)
    s.quick_sort_3(arr3)
    print(arr3)
    print(arr1 == arr2 == arr3)
