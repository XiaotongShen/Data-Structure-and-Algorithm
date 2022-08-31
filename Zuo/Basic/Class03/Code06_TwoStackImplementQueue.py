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
