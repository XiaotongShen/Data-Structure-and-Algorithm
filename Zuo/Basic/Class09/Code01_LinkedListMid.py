# -*- coding: utf-8 -*-

"""
@File: Code01_LinkedListMid.py
@Author: Sarah Shen
@Time: 20/10/2022 07:52
"""


class Node:

    def __init__(self, v: int):
        self.value = v
        self.next = None


def mid_or_up_mid_node(head):
    # 边界条件，链表上有小于等于两个节点，返回头节点
    if head is None or head.next is None or head.next.next is None:
        return head
    # 链表上有3个点或以上
    # 用快慢指针的方式实现找到中间节点
    slow = head.next
    fast = head.next.next
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def mid_or_down_mid_node(head):
    # 边界条件，链表上有最多一个节点的时候，返回头结点
    if head is None or head.next is None:
        return head
    # 链表上有2个及以上节点的时候
    # 用快慢指针的方式找到中间的或中间的第二个几点，
    # 相比上面的up_mid的方式，快指针在第一歨只向下走一步，
    # 即快指针相比之前晚一步到达最后一个节点
    # 同时慢指针多向前走一步，来到中间的第二个节点
    slow = head.next
    fast = head.next
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def mid_or_up_mid_pre_node(head):
    if head is None or head.next is None or head.next.next is None:
        return None
    slow = head  # slow晚一步
    fast = head.next.next
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def mid_or_down_mid_pre_node(head):
    if head is None or head.next is None:
        return None
    if head.next.next is None:
        return head
    slow = head
    fast = head.next
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


# 以下用容器的方法实现找到中间节点
def right1(head):
    if head is None:
        return None
    cur = head
    arr = []
    while cur is not None:
        arr.append(cur)
        cur = cur.next
    return arr[int((len(arr) - 1) / 2)]


def right2(head):
    if head is None:
        return None
    cur = head
    arr = []
    while cur is not None:
        arr.append(cur)
        cur = cur.next
    return arr[int(len(arr) / 2)]


def right3(head):
    if head is None or head.next is None or head.next.next is None:
        return None
    cur = head
    arr = []
    while cur is not None:
        arr.append(cur)
        cur = cur.next
    return arr[int((len(arr) - 3) / 2)]


def right4(head):
    if head is None or head.next is None:
        return None
    cur = head
    arr = []
    while cur is not None:
        arr.append(cur)
        cur = cur.next
    return arr[int((len(arr) - 2) / 2)]


if __name__ == "__main__":
    test = Node(0)
    test.next = Node(1)
    test.next.next = Node(2)
    test.next.next.next = Node(3)
    test.next.next.next.next = Node(4)
    test.next.next.next.next.next = Node(5)
    test.next.next.next.next.next.next = Node(6)
    test.next.next.next.next.next.next.next = Node(7)

    ans1 = mid_or_up_mid_node(test)
    ans2 = right1(test)
    print(ans1.value if ans1 is not None else "无")
    print(ans2.value if ans1 is not None else "无")

    ans1 = mid_or_down_mid_node(test)
    ans2 = right2(test)
    print(ans1.value if ans1 is not None else "无")
    print(ans2.value if ans1 is not None else "无")

    ans1 = mid_or_up_mid_pre_node(test)
    ans2 = right3(test)
    print(ans1.value if ans1 is not None else "无")
    print(ans2.value if ans1 is not None else "无")

    ans1 = mid_or_down_mid_pre_node(test)
    ans2 = right4(test)
    print(ans1.value if ans1 is not None else "无")
    print(ans2.value if ans1 is not None else "无")
