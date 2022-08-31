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
    #
    # @staticmethod
    # def check_reverse(arr: list, head: Node):
    #     """ 检查单链表是否反转正确 """
    #     index = len(arr) - 1
    #     while index > 0:
    #         if arr[index] != head.val:
    #             return False
    #         index -= 1
    #         head = head.next
    #     return True
    #
    # def main(self, times: int, max_len: int, max_val: int, func):
    #     """ 对数器主函数，随机生成单链表，并检验链表反转算法过程是否正确 """
    #     succeed = True
    #     for i in range(times):
    #         head = self.generate_random_linked_list(max_len, max_val)
    #         arr = self.transfer_linked_list_to_arr(head)
    #         head = func(head)
    #         arr_reverse = self.transfer_linked_list_to_arr(head)
    #         ans = self.check_reverse(arr, head)
    #         if not ans:
    #             succeed = False
    #             print(arr)
    #             print(arr_reverse)
    #             print('\n')
    #             break
    #
    #     print("Nice!" if succeed else "Oops, Something Went Wrong!")


if __name__ == '__main__':
    test = Test()
    a = test.generate_random_linked_list(max_len=20, max_val=5)
    print(test.transfer_linked_list_to_arr(a))
    a = remove_value(a, 4)
    print(test.transfer_linked_list_to_arr(a))
