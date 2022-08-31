# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/30.
Author: 
    Sarah Shen
Date: 
    2022/8/30
"""
# import random


class Node:
    def __init__(self, val=None, next=None, last=None):
        self.val = val
        self.next = next
        self.last = last


class DoubleEndQueue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_from_head(self, val: int):
        cur = Node(val)
        if self.head is None:
            self.head = cur
            self.tail = cur
        else:
            cur.next = self.head
            self.head.last = cur
            self.head = cur

    def add_from_bottom(self, val: int):
        cur = Node(val)
        if self.head is None:
            self.head = cur
            self.tail = cur
        else:
            cur.last = self.tail
            self.tail.next = cur
            self.tail = cur

    def pop_from_head(self):
        if self.head is None:
            return None
        else:
            cur = self.head
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                cur.next = None
                self.head.last = None
            return cur.val

    def pop_from_bottom(self):
        if self.tail is None:
            return None
        else:
            cur = self.tail
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.last
                self.tail.next = None
                cur.last = None
            return cur.val

    def is_empty(self):
        return self.head is None


class MyStack:
    def __init__(self):
        self.queue = DoubleEndQueue()

    def push(self, val: int):
        self.queue.add_from_head(val)

    def pop(self):
        self.queue.pop_from_head()

    def is_empty(self):
        return self.queue.is_empty()


class MyQueue:
    def __init__(self):
        self.queue = DoubleEndQueue()

    def push(self, val: int):
        self.queue.add_from_head(val)

    def pop(self):
        self.queue.pop_from_bottom()

    def is_empty(self):
        return self.queue.is_empty()


def is_equal(o1: int, o2: int):
    if o1 is None and o2 is not None:
        return False
    elif o1 is not None and o2 is None:
        return False
    elif o1 is None and o2 is None:
        return True
    else:
        return o1 == o2

# 测试这里待完成
# class Test:
#
#     def main(self, times:int=100000, max_laen):
