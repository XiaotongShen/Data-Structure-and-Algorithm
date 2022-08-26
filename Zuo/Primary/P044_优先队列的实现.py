# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/11.
Author: 
    Sarah Shen
Date: 
    2022/8/11
"""
import heapq

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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


if __name__ == '__main__':
    n1 = ListNode(2)
    n2 = ListNode(5)
    n3 = ListNode(7)
    n4 = ListNode(1)

    q = MyPriorityQueue()
    print(q.size())
    q.push(n1, n1.val)
    q.push(n2, n2.val)
    q.push(n3, n3.val)
    q.push(n4, n4.val)
    print(q.size())
    print(q.pop().val)
    print(q.pop().val)
    print(q.pop().val)
    print(q.pop().val)





