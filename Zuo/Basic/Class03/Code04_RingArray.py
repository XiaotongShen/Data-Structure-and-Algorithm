# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/30.
Author: 
    Sarah Shen
Date: 
    2022/8/30
"""


class RingArray:

    def __init__(self, arr=[None], push_index=0, pop_index=0, size=0, limit=0):
        self.arr = arr * limit
        self.push_index = push_index
        self.pop_index = pop_index
        self.size = size
        self.limit = limit

    def push(self, val: int):
        if self.size == self.limit:
            print("队列满了， 不能再加了")
        else:
            self.size += 1
            self.arr[self.push_index] = val
            self.push_index = self.next_index(self.push_index)

    def pop(self):
        if self.size == 0:
            print("队列空了，不能再拿了")
        else:
            self.size -= 1
            ans = self.arr[self.pop_index]
            self.arr[self.pop_index] = None
            self.pop_index = self.next_index(self.pop_index)
            return ans

    def is_empty(self):
        return self.size == 0

    def next_index(self, i: int):
        return i + 1 if i < self.limit - 1 else 0


if __name__ == '__main__':

    a = RingArray(limit=5)
    print(a.arr, a.push_index, a.pop_index, a.size, a.limit)
    a.push(0)
    print(a.arr, a.push_index, a.pop_index, a.size, a.limit)
    a.push(1)
    print(a.arr, a.push_index, a.pop_index, a.size, a.limit)
    a.push(2)
    print(a.arr, a.push_index, a.pop_index, a.size, a.limit)
    a.push(3)
    print(a.arr, a.push_index, a.pop_index, a.size, a.limit)
    a.push(4)
    print(a.arr, a.push_index, a.pop_index, a.size, a.limit)
    a.push(5)
    print(a.arr, a.push_index, a.pop_index, a.size, a.limit)
    print(a.pop())
    print(a.arr, a.push_index, a.pop_index, a.size, a.limit)
    print(a.pop())
    print(a.arr, a.push_index, a.pop_index, a.size, a.limit)
    print(a.pop())
    print(a.arr, a.push_index, a.pop_index, a.size, a.limit)
    print(a.pop())
    print(a.arr, a.push_index, a.pop_index, a.size, a.limit)
    print(a.pop())
    print(a.arr, a.push_index, a.pop_index, a.size, a.limit)
    print(a.pop())
    print(a.arr, a.push_index, a.pop_index, a.size, a.limit)

