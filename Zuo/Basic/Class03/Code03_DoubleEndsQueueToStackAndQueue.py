# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/30.
Author: 
    Sarah Shen
Date: 
    2022/8/30
"""
import random


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
        self.stack = DoubleEndQueue()

    def push(self, val: int):
        self.stack.add_from_head(val)

    def pop(self):
        return self.stack.pop_from_head()

    def is_empty(self):
        return self.stack.is_empty()


class MyQueue:
    def __init__(self):
        self.queue = DoubleEndQueue()

    def offer(self, val: int):
        self.queue.add_from_head(val)

    def poll(self):
        return self.queue.pop_from_bottom()

    def is_empty(self):
        return self.queue.is_empty()


class Stack:

    def __init__(self):
        self.stack = list()

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, val: int):
        self.stack.append(val)

    def pop(self):
        if self.is_empty():
            print("Your Stack is Empty.")
        else:
            return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Your Stack is Empty.")
        else:
            return self.stack[-1]

    def travel(self):
        if self.is_empty():
            print("Your Stack is Empty.")
        else:
            print(self.stack)


class Queue:

    def __init__(self):
        self.queue = list()

    def is_empty(self):

        return len(self.queue) == 0

    def offer(self, val: int):
        self.queue.append(val)

    def poll(self):
        if self.is_empty():
            print("Your Queue is Empty.")
        else:
            ans = self.queue[0]
            self.queue = self.queue[1:]
            return ans

    def peek(self):
        if self.is_empty():
            print("Your Queue is Empty.")
        else:
            return self.queue[0]

    def travel(self):
        if self.is_empty():
            print("Your Queue is Empty.")
        else:
            print(self.queue)


def is_equal(o1: int, o2: int):
    if o1 is None and o2 is not None:
        return False
    elif o1 is not None and o2 is None:
        return False
    elif o1 is None and o2 is None:
        return True
    else:
        return o1 == o2


class Test:

    @staticmethod
    def main(one_test_num=100, max_val=10000, times=10000):
        for i in range(times):
            my_stack = MyStack()
            my_queue = MyQueue()
            stack = Stack()
            queue = Queue()
            for j in range(one_test_num):
                num_s = int(random.random() * max_val)
                if stack.is_empty():
                    my_stack.push(num_s)
                    stack.push(num_s)
                    # stack.travel()
                else:
                    if random.random() < 0.5:
                        my_stack.push(num_s)
                        stack.push(num_s)
                    else:
                        if not is_equal(stack.pop(), my_stack.pop()):
                            print("Oops!")
                num_q = int(random.random() * max_val)
                if queue.is_empty():
                    my_queue.offer(num_q)
                    queue.offer(num_q)
                else:
                    if random.random() < 0.5:
                        my_queue.offer(num_q)
                        queue.offer(num_q)
                    else:
                        if not is_equal(queue.poll(), my_queue.poll()):
                            print("Oops!")
                            break


if __name__ == '__main__':
    t = Test()
    t.main()
