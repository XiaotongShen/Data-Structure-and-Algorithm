# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/31.
Author:
    Sarah Shen
Date:
    2022/8/31
"""


class Stack:
    """ 数组定义的Stack """

    def __init__(self, items=None):
        self.items = items

    def is_empty(self):
        return len(self.items) == 0

    def push(self, val: int):
        self.items.append(val)

    def pop(self):
        if self.is_empty():
            print("Your Stack is Empty.")
        else:
            return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("Your Stack is Empty.")
        else:
            return self.items[-1]

    def travel(self):
        if self.is_empty():
            print("Your Stack is Empty.")
        else:
            print(self.items)


class Queue:
    """ 数组定义的Queue """

    def __init__(self, items=None):
        self.items = items

    def is_empty(self):

        return len(self.items) == 0

    def offer(self, val: int):
        self.items.append(val)

    def poll(self):
        if self.is_empty():
            print("Your Queue is Empty.")
        else:
            ans = self.items[0]
            self.items = self.items[1:]
            return ans

    def peek(self):
        if self.is_empty():
            print("Your Queue is Empty.")
        else:
            return self.items[0]

    def travel(self):
        if self.is_empty():
            print("Your Queue is Empty.")
        else:
            print(self.items)


class TwoQueueStack:
    """ 两个Queue定义的Stack """

    def __init__(self, queue=Queue(items=[]), ast=Queue(items=[])):
        self.queue = queue
        self.ast = ast

    def push(self, val: int):
        self.queue.offer(val)

    def pop(self):
        while len(self.queue.items) > 1:
            self.ast.offer(self.queue.poll())
        ans = self.queue.poll()
        temp = self.queue
        self.queue = self.ast
        self.ast = temp
        return ans

    def peek(self):
        while len(self.queue.items) > 1:
            self.ast.offer(self.queue.poll())
        ans = self.queue.poll()
        self.ast.offer(ans)
        temp = self.queue
        self.queue = self.ast
        self.ast = temp
        return ans

    def is_empty(self):
        return self.queue.is_empty()

    def travel(self):
        if self.is_empty():
            print("Your Stack is Empty.")
        else:
            print(self.queue)

# 对数器待完成
