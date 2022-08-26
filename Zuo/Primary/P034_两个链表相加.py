# -*- coding: utf-8 -*-

"""
Description:
    两个链表相加
Author: 
    Sarah Shen
Date: 
    2022/8/5
"""
# 先把长链表和短链表找到
# 遍历两个链表，把长链表重定位以下


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


def list_length(head):
    """ 求链表长度 """
    length = 0
    while head is not None:
        length += 1
        head = head.next
    return length


def list_travel(head):
    """ 遍历链表中的元素 """
    if head is None:
        print("The list is empty!")
    else:
        while head is not None:
            print(head.val)
            head = head.next


def add_two_numbers(head1, head2):
    l1 = list_length(head1)
    l2 = list_length(head2)
    if l1 > l2:
        long_list = head1
        short_list = head2
    else:
        long_list = head2
        short_list = head1
    cur_l = long_list
    cur_s = short_list
    last = cur_l
    carry = 0
    # 第一阶段 长短均不空
    while cur_s is not None:
        cur_num = cur_l.val + cur_s.val + carry
        cur_l.val = (cur_num % 10)
        carry = int(cur_num / 10)
        last = cur_l
        cur_l = cur_l.next
        cur_s = cur_s.next
    # 第二阶段 长不空，短空
    while cur_l is not None:
        cur_num = cur_l.val + carry
        cur_l.val = (cur_num % 10)
        carry = int(cur_num / 10)
        last = cur_l
        cur_l = cur_l.next
    # 第三阶段 长短均为空
    if carry != 0:
        last.next = Node(1)
    return long_list


if __name__ == '__main__':
    # 定义第一个链表
    a = Node(2)
    a.next = Node(5)
    a.next.next = Node(6)
    a.next.next.next = Node(9)
    a.next.next.next.next = Node(9)
    a.next.next.next.next.next = Node(8)

    # 定义第二个链表
    b = Node(9)
    b.next = Node(2)
    b.next.next = Node(4)
    print('\nlist with head a')
    list_travel(a)
    print('\nlist with head b')
    list_travel(b)

    c = add_two_numbers(a, b)
    print('\nthe added list')
    list_travel(c)
