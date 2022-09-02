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
    """ 定义单链表 """

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def remove_value(head: Node, num: int):
    while head is not None:
        if head.val == num:
            head = head.next
        else:
            break

    pre = head
    cur = head
    while cur is not None:
        if cur.val == num:
            pre.next = cur.next
        else:
            pre = cur
        cur = cur.next
    return head


class Test:
    """ 单链表反转的对数器 """

    @staticmethod
    def generate_random_linked_list(max_len, max_val):
        """ 生成随机单链表 """
        cur_len = int(random.random() * max_len)
        if cur_len == 0:
            return None
        else:
            new_node = Node(int(random.random() * max_val))
            head = new_node
            cur = head
            cur_len -= 1
            while cur_len != 0:
                new_node = Node(int(random.random() * max_val))
                cur.next = new_node
                cur = new_node
                cur_len -= 1
            return head

    @staticmethod
    def transfer_linked_list_to_arr(head: Node):
        """ 将单链表val按依次放入数组 """
        ans = []
        while head is not None:
            ans.append(head.val)
            head = head.next
        return ans


if __name__ == '__main__':
    test = Test()
    a = test.generate_random_linked_list(max_len=20, max_val=5)
    print(test.transfer_linked_list_to_arr(a))
    a = remove_value(a, 4)
    print(test.transfer_linked_list_to_arr(a))
