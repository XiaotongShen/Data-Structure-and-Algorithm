# -*- coding: utf-8 -*-

"""
@File: Code01_FindFirstIntersectNode.py
@Author: Sarah Shen
@Time: 21/10/2022 15:29
"""


# 题目，两个单链表，可能有环，可能无环，找到两个链表第一个相交的节点
# 将问题拆分，首先判断每个链表是否有环：
# 判断是否有环，使用快慢指针，只要快指针的next，和next.next均不为空（若为空了，无环)，则找到快指针和慢指针相同的节点
# 慢指针不动，快指针回到头结点，继续移动快慢节点，两个指针再次相同的节点为入环的节点（这里好神奇，但是课上没有证明）

# 第一个相交节点的分情况讨论
# p1 两个链表无环，找到各自最后一个节点，如果最后一个节点不相同，说明不相交，从头遍历，长链表先走，
# 来找到第一个相同的节点，返回
# p2 一个节点有环，一个节点无环，此时两个链表不可能相交
# p3 两个链表均有环：...


class Node:

    def __init__(self, v: int):
        self.value = v
        self.next = None


def get_intersect_node(head1, head2):
    if head1 is None or head2 is None:
        return None
    loop1 = get_loop_node(head1)
    loop2 = get_loop_node(head2)
    if loop1 is None and loop2 is None:
        return no_loop(head1, head2)
    if loop1 is not None and loop2 is not None:
        return both_loop(head1, loop1, head2, loop2)
    return None


def get_loop_node(head):
    """ 找到单链表中的入环节点, 如果无环，返回None """
    if head is None or head.next is None or head.next.next is None:
        return None
    # 快慢指针
    slow = head.next
    fast = head.next.next
    while slow != fast:
        if fast.next is None or fast.next.next is None:
            return None
        slow = slow.next
        fast = fast.next.next
        # 以上没有return的话，slow = fast
    fast = head  # 慢指针不动，快指针回到头节点
    # 继续移动快慢指针，下一个相遇的节点是入环节点
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


def no_loop(head1, head2):
    """ 如果两个链表都无环，返回第一个相交节点，如果都不想交，返回None """
    # 边界条件，两个头节点都为空，不可能有相交节点，返回空
    if head1 is None or head2 is None:
        return None
    cur1 = head1
    cur2 = head2
    n = 0
    # 第一个链表从头遍历结束，来到最后一个节点
    while cur1.next is not None:
        n += 1
        cur1 = cur1.next
    # 第二个链表从头遍历结束，来到最后一个节点
    while cur2.next is not None:
        n -= 1
        cur2 = cur2.next
    # 如果两个终节点不相同，表示无相交，返回空
    if cur1 != cur2:
        return None
    # 否则判断长短链表，复用变量
    # 如果n为正数，表示head1为长链表，否则head2为长链表，cur保留长链表的头
    cur1 = head1 if n > 0 else head2
    # cur2保存短链表，如果head1为长链表（cur1 == head1）,那么head2为短链表，放入cur2
    cur2 = head2 if cur1 == head1 else head1
    n = abs(n)  # 取n的绝对值
    # 长链表先遍历n步
    while n != 0:
        # print(n)
        n -= 1
        cur1 = cur1.next
    # 以上遍历结束后，长短链表剩余遍历长度一致，同时遍历，直到找到第一个相同的节点，即为所求
    while cur1 != cur2:
        cur1 = cur1.next
        cur2 = cur2.next
    return cur1


def both_loop(head1, loop1, head2, loop2):
    """ 两个有环链表，返回第一个相交节点，如果不相交，返回None """
    # 情况1：两个单链表入环节点一致, 将入环节点当做两链表的终节点，复用no_loop的逻辑
    if loop1 == loop2:
        cur1 = head1
        cur2 = head2
        n = 0
        # 分别从头开始遍历，找到长短链表
        while cur1 != loop1:
            n += 1
            cur1 = cur1.next
        while cur2 != loop2:
            n -= 1
            cur2 = cur2.next
        # cur1 -> 长链表头节点，cur2 -> 短链表头节点
        cur1 = head1 if n > 0 else head2
        cur2 = head2 if cur1 == head1 else head1
        n = abs(n)
        # 长链表提前遍历n步
        while n != 0:
            n -= 1
            cur1 = cur1.next
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1
    else:
        # 其他情况：可能不相交，可能入环节点不是一个
        cur1 = loop1.next
        while cur1 != loop1:
            # 链表1在还内遍历一圈
            if cur1 == loop2:
                # 如果环内有loop2，即链表2的入环几点，表示有相交，第一个相交的节点是loop1或loop2
                return loop1
            # print(cur1.value)
            cur1 = cur1.next
        # 如果链表1在环内遍历一圈，没发现loop2，表示无相交节点
        return None


if __name__ == '__main__':
    # 1->2->3->4->5->6->7->None
    h1 = Node(1)
    h1.next = Node(2)
    h1.next.next = Node(3)
    h1.next.next.next = Node(4)
    h1.next.next.next.next = Node(5)
    h1.next.next.next.next.next = Node(6)
    h1.next.next.next.next.next.next = Node(7)

    # loop1 = get_loop_node(h1)
    # print("入环节点loop1:")
    # print(loop1)

    # 0->9->8->6->7->None
    h2 = Node(0)
    h2.next = Node(9)
    h2.next.next = Node(8)
    h2.next.next.next = h1.next.next.next.next.next  # 8->6
    #
    # loop2 = get_loop_node(h1)
    # print("入环节点loop2:")
    # print(loop2)

    print(get_intersect_node(h1, h2).value)

    # 1->2->3->4->5->6->7->4...
    h3 = Node(1)
    h3.next = Node(2)
    h3.next.next = Node(3)
    h3.next.next.next = Node(4)
    h3.next.next.next.next = Node(5)
    h3.next.next.next.next.next = Node(6)
    h3.next.next.next.next.next.next = Node(7)
    h3.next.next.next.next.next.next = h3.next.next.next  # 7->4
    # print("入环节点loop3:")
    # print(get_loop_node(h3).value)

    # 0->9->8->2...
    h4 = Node(0)
    h4.next = Node(9)
    h4.next.next = Node(8)
    h4.next.next.next = h3.next  # 8->2
    # print("入环节点loop4:")
    # print(get_loop_node(h4).value)

    print(get_intersect_node(h3, h4).value)

    # 0->9->8->6->4->5->6..
    h5 = Node(0)
    h5.next = Node(9)
    h5.next.next = Node(8)
    h5.next.next.next = h3.next.next.next.next.next  # 8->6
    # print("入环节点loop5:")
    # print(get_loop_node(h5).value)

    print(get_intersect_node(h3, h5).value)
