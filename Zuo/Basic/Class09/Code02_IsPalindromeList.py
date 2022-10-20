# -*- coding: utf-8 -*-

"""
@File: Code02_IsPalindromeList.py
@Author: Sarah Shen
@Time: 20/10/2022 07:53
"""


class Node:

    def __init__(self, v: int):
        self.value = v
        self.next = None


def is_palindrome1(head):
    """ 用容器栈判断 """
    # 需要额外空间n, 将全部节点压入栈，依次弹出比较
    stack = []
    cur = head
    while cur is not None:
        stack.append(cur)
        cur = cur.next
    while head is not None:
        if head.value != stack.pop().value:
            return False
        head = head.next
    return True


def is_palindrome2(head):
    """ 用容器栈判断 """
    # 需要额外空间n/2，找到中点，只将中点之后的节点压入栈，弹出比较
    if head is None or head.next is None:
        return True
    # 用快慢指针的方法，快指针cur，满指针right，找到链表的中点right
    right = head.next
    cur = head
    while cur.next is not None and cur.next.next is not None:
        right = right.next
        cur = cur.next.next
    # 将从中点开始的node压入栈
    stack = []
    while right is not None:
        stack.append(right)
        right = right.next
    # 从栈中依次弹出节点，与原链表从头结点开始的值作比较
    while len(stack) > 0:
        if head.value != stack.pop().value:
            return False
        head = head.next
    return True


def is_palindrome3(head):
    # 需要额外空间O(1)
    if head is None or head.next is None:
        return True
    n1 = head
    n2 = head
    # 使用快慢指针的方式，找到中点
    while n2.next is not None and n2.next.next is not None:
        n1 = n1.next
        n2 = n2.next.next
    # n1为中点，复用变量
    n2 = n1.next  # right part first node
    n1.next = None  # mid.next -> None
    # 将中点右侧部分逆序
    while n2 is not None:
        n3 = n2.next
        n2.next = n1
        n1 = n2
        n2 = n3
    # 再次复用变量，
    n3 = n1  # n3 -> 最后一个节点，即反转后的右侧链表的头，保存在n3中
    n2 = head  # n2 -> 头节点，即中点左侧量表的头节点
    # 开始检查回文
    res = True
    while n1 is not None and n2 is not None:
        if n1.value != n2.value:
            res = False
            break
        n1 = n1.next  # left head to mid
        n2 = n2.next  # right head to mid
    # 复用变量，将链表调回原样
    n1 = n3.next
    n3.next = None
    while n1 is not None:
        n2 = n1.next
        n1.next = n3
        n3 = n1
        n1 = n2
    return res


def print_linked_list(head):
    print("Linked_list: ")
    while head is not None:
        print(str(head.value) + " ")
        head = head.next
    print()


if __name__ == "__main__":
    test = Node(0)
    test.next = Node(1)
    test.next.next = Node(2)
    test.next.next.next = Node(3)
    test.next.next.next.next = Node(4)
    test.next.next.next.next.next = Node(5)
    test.next.next.next.next.next.next = Node(6)
    test.next.next.next.next.next.next.next = Node(7)

    p = Node(0)
    p.next = Node(1)
    p.next.next = Node(2)
    p.next.next.next = Node(3)
    p.next.next.next.next = Node(2)
    p.next.next.next.next.next = Node(1)
    p.next.next.next.next.next.next = Node(0)

    print_linked_list(test)
    print_linked_list(p)

    print(is_palindrome1(test))
    print(is_palindrome1(p))
    print()

    print(is_palindrome2(test))
    print(is_palindrome2(p))
    print()

    print(is_palindrome3(test))
    print(is_palindrome3(p))
    print()
    # a = []
    # a.append(0)
    # a.append(1)
    # a.append(2)
    # a.append(3)
    # print(a)
    # for i in range(len(a)):
    #     print(a[i])
    # print(a.pop())
    # print(a.pop())
    # print(a.pop())
    # print(a.pop())
