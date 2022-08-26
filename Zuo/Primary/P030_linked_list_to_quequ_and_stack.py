# -*- coding: utf-8 -*-

"""
Description:
    通过单链表实现队列和栈
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


class MyQueue:
    """ 单链表实现的队列"""
    def __init__(self):
        """ 初始化一个空的队列 """
        self.head = None  # 头指针
        self.tail = None  # 尾指针
        self.size = 0  # 队列长度

    def is_empty(self):
        """ 返回队列是否为空 """
        return self.size == 0

    def len(self):
        print('The Length of Queue is ', self.size)

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

    def push(self, value):
        """ 向队列压入一个新的节点，值为value"""
        n = Node(value)
        if self.size == 0:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n
        self.size += 1
        print('Push %i to Queue' % value)

    def pop(self):
        """ 从队列弹出一个节点 """
        v = None
        if self.head is not None:
            n = self.head
            v = n.value
            self.head = n.next
            if self.head is None:
                self.tail = None
            self.size -= 1

        print('Pop once from Queue, the value is %s' % str(v))


class MyStack:

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        """ 返回栈是否为空 """
        return self.size == 0

    def len(self):
        print('The Length of Stack is ', self.size)

    def first(self):
        """ 返回栈首节点的值"""
        if self.is_empty():
            print("This Stack is Empty!")
        else:
            print('The first value of Stack is', self.head.value)

    def push(self, value):
        """ 向队列压入一个新的节点，值为value"""
        n = Node(value)
        if self.size == 0:
            self.head = n
        else:
            n.next = self.head
            self.head = n
        self.size += 1
        print('Push %i to Stack' % value)

    def pop(self):
        """ 从队列弹出一个节点 """
        v = None
        if self.head is not None:
            n = self.head
            v = n.value
            self.head = n.next
            self.size -= 1
        print('Pop once from Stack, the value is %s' % str(v))


if __name__ == '__main__':
    # q = MyQueue()
    # print(q.is_empty())
    # q.len()
    #
    # for i in range(5):
    #     print('\n')
    #     q.push(i)
    #     q.len()
    #     q.first()
    #     q.last()
    #
    # for i in range(5):
    #     print('\n')
    #     q.pop()
    #     q.len()
    #     q.first()
    #     q.last()
    #
    # print('\n')
    # print(q.is_empty())
    # q.len()

    s = MyStack()
    print(s.is_empty())
    s.len()

    for i in range(5):
        print('\n')
        s.push(i)
        s.len()
        s.first()

    for i in range(5):
        print('\n')
        s.pop()
        s.len()
        s.first()

    print('\n')
    print(s.is_empty())
    s.len()
