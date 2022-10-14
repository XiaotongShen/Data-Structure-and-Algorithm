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


class TwoStackQueue:
    def __init__(self, stack_push=Stack(items=[]), stack_pop=Stack(items=[])):
        self.stack_push = stack_push
        self.stack_pop = stack_pop

    def push_to_pop(self):
        if self.stack_pop.is_empty():
            while not self.stack_push.is_empty():
                self.stack_pop.push(self.stack_push.pop())

    def add(self, val: int):
        self.stack_push.push(val)
        self.push_to_pop()

    def poll(self):
        if self.stack_pop.is_empty() and self.stack_push.is_empty():
            print("Queue is Empty!")
        else:
            self.push_to_pop()
            return self.stack_pop.pop()

    def peek(self):
        if self.stack_pop.is_empty() and self.stack_push.is_empty():
            print("Queue is Empty!")
        else:
            self.push_to_pop()
            return self.stack_pop.peek()


if __name__ == '__main__':
    test = TwoStackQueue()
    test.add(1)
    test.add(2)
    test.add(3)
    print(test.peek())
    print(test.poll())
    print(test.peek())
    print(test.poll())
    print(test.peek())
    print(test.poll())
