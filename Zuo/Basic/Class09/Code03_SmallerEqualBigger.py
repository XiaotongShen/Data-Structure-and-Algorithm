# -*- coding: utf-8 -*-

"""
@File: Code03_SmallerEqualBigger.py
@Author: Sarah Shen
@Time: 20/10/2022 07:54
"""


class Node:

    def __init__(self, v: int):
        self.value = v
        self.next = None


def list_partition1(head, pivot: int):
    if head is None:
        return head
    cur = head
    i = 0
    # 检查链表中节点的个数
    while cur is not None:
        i += 1
        cur = cur.next
    node_arr = [Node(0)] * i
    cur = head
    # 将节点依次放入list中
    for i in range(len(node_arr)):
        node_arr[i] = cur
        cur = cur.next
    # 对list中的节点分区，小于，等于，大于
    arr_partition(node_arr, pivot)
    # 依次调整排好序的节点的指针关系，i-1 -> i
    for i in range(1, len(node_arr)):
        node_arr[i - 1].next = node_arr[i]
    node_arr[i].next = None
    # 返回list中的第一个节点，即头节点
    return node_arr[0]


def arr_partition(arr: list, pivot: int):
    small = -1
    big = len(arr)
    index = 0
    while index != big:
        if arr[index].value < pivot:
            small += 1
            swap(arr, small, index)
            index += 1
        elif arr[index] == pivot:
            index += 1
        else:
            big -= 1
            swap(arr, big, index)
            index += 1


def swap(arr: list, a: int, b: int):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def list_partition2(head, pivot: int):
    sh = None  # small head
    st = None  # small tail
    eh = None  # equal head
    et = None  # equal tail
    bh = None  # big head
    bt = None  # big tail
    # Every Node Distributed to three list
    while head is not None:
        nxt = head.next
        head.next = None
        if head.value < pivot:
            if sh is None:
                sh = head
                st = head
            else:
                st.next = head
                st = head
        elif head.value == pivot:
            if eh is None:
                eh = head
                et = head
            else:
                et.next = head
                et = head
        else:
            if bh is None:
                bh = head
                bt = head
            else:
                bt.next = head
                bt = head
        head = nxt
        # 到这里，所有的节点已经被分配到小于，等于和大于三个list中
    if st is not None:
        # 有小于区域
        st.next = eh
        et = st if et is None else et
    # 下一步，谁去连大于区域的头，谁就变成et
    # 下一步，一定是要用et 去接 bh
    # 有等于区域，et：等于区域的尾节点
    # 无等于区域，et：小于区域的尾节点
    # et 是尽量不为空的尾节点
    if et is not None:
        et.next = bh

    return sh if sh is not None else (eh if eh is not None else bh)


def print_linked_list(head):
    print("Linked List: ")
    while head is not None:
        print(str(head.value) + " ")
        head = head.next
    print()


if __name__ == "__main__":
    head1 = Node(7)
    head1.next = Node(9)
    head1.next.next = Node(1)
    head1.next.next.next = Node(8)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = Node(2)
    head1.next.next.next.next.next.next = Node(5)

    print_linked_list(head1)

    # head1 = list_partition1(head1, 5)
    head1 = list_partition2(head1, 5)
    print_linked_list(head1)
