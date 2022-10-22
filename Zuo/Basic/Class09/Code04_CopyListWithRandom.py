# -*- coding: utf-8 -*-

"""
@File: Code04_CopyListWithRandom.py
@Author: Sarah Shen
@Time: 20/10/2022 07:54
"""


class Node:

    def __int__(self, v: int):
        self.value = v
        self.next = None
        self.random = None


def copy_random_list1(head):
    list_map = dict()
    cur = head
    while cur is not None:
        list_map[cur] = Node(cur.value)
        cur = cur.next
    cur = head
    while cur is not None:
        # cur 老链表的节点
        # map.get(cur) 复制出来额新节点
        # 新.next -> cur.next 克隆节点的next找到
        list_map.get(cur).next = cur.next
        list_map.get(cur).random = cur.random
        cur = cur.next
    return list_map.get(head)


def copy_random_list2(head):
    if head is None:
        return None
    cur = head
    while cur is not None:
        nxt = cur.next
        cur.next = Node(cur.value)
        cur.next.next = nxt
        cur = nxt
    cur = head
    while cur is not None:
        nxt = cur.next.next
        copy = cur.next
        copy.random = cur.random if cur.random is not None else None
        cur = nxt
    res = head.next
    cur = head
    while cur is not None:
        nxt = cur.next.next
        copy = cur.next
        cur.next = nxt
        copy.next = nxt.next if nxt is not None else None
        cur = nxt
    return res


if __name__ == '__main__':
    d = dict()
    d[1] = "a"
    d[2] = "b"
    print(d)
    print(d.get(1))
    print(d)
