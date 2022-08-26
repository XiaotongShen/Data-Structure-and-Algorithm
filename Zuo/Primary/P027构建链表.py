# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/7/26.
Author: 
    Sarah Shen
Date: 
    2022/7/26
"""


class Node:
    """ 节点，保存数据和后续节点 """
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        """ 判断链表是否为空 """
        return self.head is None

    def travel(self):
        """ 遍历链表 """
        cur = self.head
        while cur is not None:
            print(cur.value)
            cur = cur.next

    def length(self):
        """ 返回链表长度 """
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def append(self, value):
        """ 在链表尾部添加节点 """
        node = Node(value)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def add(self, value):
        """ 在链表头部添加节点 """
        node = Node(value)

        node.next = self.head
        self.head = node

    def insert(self, pos, value):
        """ 在指定位置插入节点 """
        if pos <= 0:
            # 如果pos < 0, 则认为在头部插入
            self.add(value)
        elif pos > self.length() - 1:
            # 如果pos大于链表长度，则认为在尾部插入
            self.append(value)
        else:
            # 从头部开始找到指定位置
            pre = self.head
            count = 0
            while count < pos - 1:
                count += 1
                pre = pre.next

            #  插入节点到pre 和 pre.next中间，即设node的next = pre的next，再令pre的next = node
            node = Node(value)
            node.next = pre.next
            pre.next = node

    def search(self, value):
        """ 查找节点是否存在 """
        cur = self.head

        while cur is not None:
            if cur.value == value:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, value):
        pre = self.head

        if pre.value == value:
            self.head = pre.next
        else:
            # 找到删除节点的前驱节点
            while pre.next.value != value:
                pre = pre.next
            pre.next = pre.next.next


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        """ 判断链表是否为空 """
        return self.head is None

    def travel(self):
        """ 遍历链表 """
        cur = self.head
        while cur is not None:
            print(cur.value)
            cur = cur.next

    def length(self):
        """ 返回链表长度 """
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def append(self, value):
        """ 在链表尾部添加节点 """
        node = Node(value)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.pre = cur

    def add(self, value):
        """ 在链表头部添加节点 """
        node = Node(value)

        self.head.pre = node
        node.next = self.head
        self.head = node

    def insert(self, pos, value):
        """ 在指定位置插入节点 """
        if pos <= 0:
            # 如果pos < 0, 则认为在头部插入
            self.add(value)
        elif pos > self.length() - 1:
            # 如果pos大于链表长度，则认为在尾部插入
            self.append(value)
        else:
            # 从头部开始找到指定位置
            pre = self.head
            count = 0
            while count < pos - 1:
                count += 1
                pre = pre.next

            #  插入节点到pre 和 pre.next中间，即设node的next = pre的next，再令pre的next = node
            node = Node(value)
            node.next = pre.next
            node.pre = pre
            pre.next = node
            node.next.pre = node

    def search(self, value):
        """ 查找节点是否存在 """
        cur = self.head

        while cur is not None:
            if cur.value == value:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, value):
        pre = self.head

        if pre.value == value:
            self.head = pre.next
            pre.next.pre = None
        else:
            # 找到删除节点的前驱节点
            while pre.next.value != value:
                pre = pre.next

            if pre.next.next is not None:
                pre.next.next.pre = pre
            pre.next = pre.next.next


def reverse_linked_list(head):
    pre = None
    while head is not None:
        nxt = head.next
        head.next = pre
        pre = head
        head = nxt
    return pre

def reverse_double_linked_list(head):
    while head is not None:
        pr = head.pre
        nxt = head.next
        head.pre = nxt
        head.next = pr
        pr = head
        head = nxt
    return pr



if __name__ == '__main__':

    # ll = LinkedList()
    # ll.append(1)
    # ll.append(2)
    # ll.append(3)
    # ll.append(4)
    # ll.append(5)
    # ll.append(6)
    # ll.add(0)
    #
    # print("\n反转前的链表：")
    # ll.travel()
    # print("head是：")
    # print(ll.head.value)
    #
    # ll.head = reverse_linked_list(ll.head)
    #
    # print("\n反转后的链表：")
    # ll.travel()
    # print("head是：")
    # print(ll.head.value)

    dl = DoubleLinkedList()
    dl.append(0)
    dl.append(1)
    dl.append(2)

    print(dl.length())
    print("\n创建的双链表为：")
    dl.travel()

    print("\n双链表的第二个值为：")
    print(dl.head.next.value)
    print("双链表的第二个值的下一个值为：")
    print(dl.head.next.next.value)
    print("双链表的第二个值的上一个值为：")
    print(dl.head.next.pre.value)

    dl.head = reverse_double_linked_list(dl.head)

    print("\n反转后双链表为：")
    dl.travel()

    print("\n反转后双链表的第二个值为：")
    print(dl.head.next.value)
    print("反转后双链表的第二个值的下一个值为：")
    print(dl.head.next.next.value)
    print("反转后双链表的第二个值的上一个值为：")
    print(dl.head.next.pre.value)






