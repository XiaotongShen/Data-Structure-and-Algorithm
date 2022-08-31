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


class MyStack:

    def __init__(self, data_stack=Stack(items=[]), min_stack=Stack(items=[])):
        self.data_stack = data_stack
        self.min_stack = min_stack

    def push(self, val: int):
        if self.min_stack.is_empty():
            self.min_stack.push(val)
        else:
            self.min_stack.push(min(val, self.get_min()))

        self.data_stack.push(val)

    def pop(self):
        if self.data_stack.is_empty():
            print("Your Stack is Empty.")
        else:
            self.min_stack.pop()
            return self.data_stack.pop()

    def get_min(self):
        if self.min_stack.is_empty():
            print("Your Stack is Empty.")
        else:
            return self.min_stack.peek()

    def travel(self):
        if self.data_stack.is_empty():
            print("Your Stack is Empty.")
        else:
            self.data_stack.travel()


if __name__ == '__main__':
    s = MyStack()
    s.travel()
    print(s.get_min())
    print("===============")
    s.push(3)
    s.travel()
    print(s.get_min())
    print("===============")
    s.push(4)
    s.travel()
    print(s.get_min())
    print("===============")
    s.push(1)
    s.travel()
    print(s.get_min())
    print("===============")
    s.push(9)
    s.travel()
    print(s.get_min())
    print("===============")
    s.push(2)
    s.travel()
    print(s.get_min())
    print("===============")
    s.push(0)
    s.travel()
    print(s.get_min())
    print("===============")
    s.pop()
    s.travel()
    print(s.get_min())
    print("===============")
    s.pop()
    s.travel()
    print(s.get_min())
    print("===============")
    s.pop()
    s.travel()
    print(s.get_min())
    print("===============")
    s.pop()
    s.travel()
    print(s.get_min())
    print("===============")
    s.pop()
    s.travel()
    print(s.get_min())
    print("===============")
    s.pop()
    s.travel()
    print(s.get_min())
    print("===============")
