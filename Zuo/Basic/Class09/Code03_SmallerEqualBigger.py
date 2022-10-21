# -*- coding: utf-8 -*-

"""
@File: Code03_SmallerEqualBigger.py
@Author: Sarah Shen
@Time: 20/10/2022 07:54
"""
# TODO: 09-03待完成


class Node:

    def __init__(self, v: int):
        self.value = v
        self.next = None


def list_partition1(head, pivot: int):
    print(head.value, pivot)


def arr_partition(arr: list, pivot: int):
    print(arr, pivot)


def swap(arr: list, a: int, b: int):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def list_partition2(head, pivot: int):
    print(pivot, head.value)


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
