# -*- coding: utf-8 -*-

"""
Description:
    使用双链表实现双端队列
Author: 
    Sarah Shen
Date: 
    2022/8/4
"""


class Node:
    """ 节点，保存数据和后续节点 """

    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None


class MyDQueue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def len(self):
        print(self.size)

    def first(self):
        """ 返回队列首节点的值"""
        if self.is_empty():
            print("This Queue is Empty!")
        else:
            print('The first value of Queue is', self.head.value)

    def last(self):
        """ 返回队列尾节点的值"""
        if self.is_empty():
            print("This Queue is Empty!")
        else:
            print('The last value of Queue is', self.tail.value)

    def push_head(self, value):
        n = Node(value)
        if self.is_empty():
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head.pre = n
            self.head = n
        self.size += 1

    def push_tail(self, value):
        n = Node(value)
        if self.is_empty():
            self.tail = n
            self.head = n
        else:
            n.pre = self.tail
            self.tail.next = n
            self.tail = n
        self.size += 1

    def pop_head(self):
        ans = None
        if self.is_empty():
            return ans
        else:
            self.size -= 1
            ans = self.head.value
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                n = self.head
                self.head = n.next
                n.next.pre = None
                n.next = None
            return ans

    def pop_tail(self):
        ans = None
        if self.is_empty():
            return ans
        else:
            self.size -= 1
            ans = self.tail
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                n = self.tail
                self.tail = n.pre
                n.pre.next = None
                n.pre = None
            return ans



if __name__ == '__main__':
    q = MyDQueue()
    print(q.is_empty())
    q.len()

    for i in range(5):
        print('\n')
        q.push_head(i)
        q.len()
        q.first()
        q.last()

    for i in range(5):
        print('\n')
        q.pop_head()
        q.len()
        q.first()
        q.last()

    for i in range(5):
        print('\n')
        q.push_tail(i)
        q.len()
        q.first()
        q.last()

    for i in range(5):
        print('\n')
        q.pop_tail()
        q.len()
        q.first()
        q.last()

    print('\n')
    print(q.is_empty())
    q.len()