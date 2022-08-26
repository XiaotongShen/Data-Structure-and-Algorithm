# -*- coding: utf-8 -*-

"""
Description:
    合并两个有序链表
Author: 
    Sarah Shen
Date: 
    2022/8/5
"""


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


def travel(head):
    """ 遍历链表中的元素 """
    if head is None:
        print("The list is empty!")
    else:
        while head is not None:
            print(head.val)
            head = head.next


def merge_two_sorted_lists(head1, head2):
    """ 合并两个有序链表 """
    # 边界条件：其中一个链表为空，返回另一个链表
    if head1 is None or head2 is None:
        return head1 if head2 is None else head2
    else:
        if head1.val <= head2.val:
            head = head1
            cur1 = head1.next
            cur2 = head2
        else:
            head = head2
            cur1 = head1
            cur2 = head2.next
        pre = head
        while cur1 is not None and cur2 is not None:
            if cur1.val <= cur2.val:
                pre.next = cur1
                cur1 = cur1.next
            else:
                pre.next = cur2
                cur2 = cur2.next
            pre = pre.next
        pre.next = cur2 if cur1 is None else cur1
    return head


if __name__ == '__main__':
    h1 = Node(1)
    h1.next = Node(5)
    h1.next.next = Node(7)

    h2 = Node(2)
    h2.next = Node(6)
    h2.next.next = Node(9)

    print('\n第一个有序链表')
    travel(h1)
    print('\n第二个有序链表')
    travel(h2)

    h3 = merge_two_sorted_lists(h1, h2)
    print('\n合并后的有序链表')
    travel(h3)
