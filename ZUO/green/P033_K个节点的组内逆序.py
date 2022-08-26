# -*- coding: utf-8 -*-

"""
Description:
    K个节点的组内逆序，这一个主题属于困难题，要细致，锻炼代码实现能力
Author: 
    Sarah Shen
Date: 
    2022/8/5
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


def get_group_end(start, k):
    """ 给定头节点，返回长度为k的一组节点的尾节点"""
    while k != 0 and start is not None:
        start = start.next
        k -= 1
    return start


def reverse(start, end):
    end = end.next
    pre = None
    cur = start
    nxt = None
    if cur != end:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    start.next = end


def revers_k_group(head, k):
    start = head
    end = get_group_end(start, k)
    if end is None:
        return head
    # 第一组凑齐了
    head = end
    reverse(start, end)
    last_end = start

    while last_end.next is not None:
        start = last_end.next
        end = end = get_group_end(start, k)
        if end is None:
            return head
        reverse(start, end)
        last_end.next = end
        last_end = start

    return head



if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    print(b.next.value)

