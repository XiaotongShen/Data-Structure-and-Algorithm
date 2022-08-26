# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/9.
Author: 
    Sarah Shen
Date: 
    2022/8/9
"""
# 解题思路，利用小根堆：
# 首先将M个头节点放入小根堆，最小值弹出
# 将最小值的next放入小根堆，最小值弹出
# ...以此类推，直至小根堆中的节点全部弹出

import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyPriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        """
        优先级队列由item，index，priority组成：
        item是队列中实际存储的对象，
        priority是对象进行优先级比较的元素
        index是为了当两个对象优先级一只的时候，按照插入顺序排序
        """
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        """ 弹出优先级最高的对象 """
        return heapq.heappop(self._queue)[-1]

    def size(self):
        return len(self._queue)

    def is_empty(self):
        return self.size() == 0


# class Solution:
def merge_k_list(lists):
    heap = MyPriorityQueue()
    for node in lists:
        heap.push(node, node.val)
    head = heap.pop()
    nxt = head.next
    heap.push(nxt, nxt.val)
    pre = head
    while heap.size() > 0:
        cur = heap.pop()
        pre.next = cur
        nxt = cur.next
        if nxt is not None:
            heap.push(nxt, nxt.val)
        else:
            pass
        pre = cur
    return head


if __name__ == '__main__':

    n1 = ListNode(1)
    n1.next = ListNode(3)
    n1.next.next = ListNode(5)

    n2 = ListNode(2)
    n2.next = ListNode(7)
    n2.next.next = ListNode(9)

    n3 = ListNode(4)
    n3.next = ListNode(6)
    n3.next.next = ListNode(8)

    list_heads = [n1, n2, n3]
    h = merge_k_list(list_heads)
    print(h.val)

