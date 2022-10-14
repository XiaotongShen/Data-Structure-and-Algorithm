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
    """ 定义单链表类 """

    def __init__(self, val=None, nxt=None):
        self.val = val
        self.next = nxt


def reverse_ll(head: Node):
    """ 单链表反转 """
    pre = None
    while head is not None:
        nxt = head.next
        head.next = pre
        pre = head
        head = nxt
    return pre


class DoubleNode:
    """ 定义双链表类 """

    def __init__(self, val=None, nxt=None, pre=None):
        self.val = val
        self.next = nxt
        self.pre = pre


def reverse_dl(head: DoubleNode):
    """ 双链表反转 """
    pre = None
    while head is not None:
        nxt = head.next
        head.next = pre
        head.pre = nxt
        pre = head
        head = nxt
    return pre


class TestReverseLinkedList:
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

    @staticmethod
    def check_reverse(arr: list, head: Node):
        """ 检查单链表是否反转正确 """
        index = len(arr) - 1
        while index > 0:
            if arr[index] != head.val:
                return False
            index -= 1
            head = head.next
        return True

    def main(self, times: int, max_len: int, max_val: int, func):
        """ 对数器主函数，随机生成单链表，并检验链表反转算法过程是否正确 """
        succeed = True
        for i in range(times):
            head = self.generate_random_linked_list(max_len, max_val)
            arr = self.transfer_linked_list_to_arr(head)
            head = func(head)
            arr_reverse = self.transfer_linked_list_to_arr(head)
            ans = self.check_reverse(arr, head)
            if not ans:
                succeed = False
                print(arr)
                print(arr_reverse)
                print('\n')
                break

        print("Nice!" if succeed else "Oops, Something Went Wrong!")


class TestReverseDoubleLinkedList:
    """ 双链表反转的对数器 """

    @staticmethod
    def generate_random_double_linked_list(max_len, max_val):
        """ 生成随机单链表 """
        cur_len = int(random.random() * max_len)
        if cur_len == 0:
            return None
        else:
            head = DoubleNode(int(random.random() * max_val))
            pre = head
            cur_len -= 1
            while cur_len != 0:
                cur = DoubleNode(int(random.random() * max_val))
                pre.next = cur
                cur.pre = pre
                pre = cur
                cur_len -= 1
            return head

    @staticmethod
    def transfer_linked_list_to_arr(head: DoubleNode):
        """ 将单链表val按依次放入数组 """
        ans = []
        while head is not None:
            ans.append(head.val)
            head = head.next
        return ans

    @staticmethod
    def check_reverse(arr: list, head: Node):
        """ 检查单链表是否反转正确 """
        index = len(arr) - 1
        while index > 0:
            if arr[index] != head.val:
                return False
            index -= 1
            head = head.next
        return True

    def main(self, times: int, max_len: int, max_val: int, func):
        """ 对数器主函数，随机生成单链表，并检验链表反转算法过程是否正确 """
        succeed = True
        for i in range(times):
            head = self.generate_random_double_linked_list(max_len, max_val)
            arr = self.transfer_linked_list_to_arr(head)
            head = func(head)
            arr_reverse = self.transfer_linked_list_to_arr(head)
            ans = self.check_reverse(arr, head)
            if not ans:
                succeed = False
                print(arr)
                print(arr_reverse)
                print('\n')
                break

        print("Nice!" if succeed else "Oops, Something Went Wrong!")


if __name__ == '__main__':
    test_single = TestReverseLinkedList()
    test_single.main(times=100000, max_len=20, max_val=30, func=reverse_ll)

    test_double = TestReverseDoubleLinkedList()
    test_double.main(times=100000, max_len=20, max_val=30, func=reverse_dl)
