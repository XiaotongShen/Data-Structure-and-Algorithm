# -*- coding: utf-8 -*-

"""
@File: Code03_TopologicalOrderDFS1.py
@Author: Sarah Shen
@Time: 25/10/2022 17:12
"""
# OJ链接：https://www.lintcode.com/problem/topological-sorting


class DirectedGraphNode:

    def __init__(self, x):
        self.label = x
        self.neighbors = list()


class Record:

    def __init__(self, n: DirectedGraphNode, o: int):
        self.node = n
        self.deep = o


def my_comparator(o1: Record, o2: Record):
    return o2.deep - o1.deep


def cmp_to_key(mycmp):
    """
    Convert a cmp= function into a key= function
    """

    class K:
        def __init__(self, obj):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0

    return K


def top_sort(graph):
    order = dict()
    for cur in graph:
        f(cur, order)
    record_arr = list()
    for r in order.values():
        record_arr.append(r)
    record_arr.sort(key=cmp_to_key(my_comparator))
    ans = list()
    for r in record_arr:
        ans.append(r.node)
    return ans


def f(cur: DirectedGraphNode, order: dict):
    if order.keys().__contains__(cur):
        return order.get(cur)
    follow = 0
    for nxt in cur.neighbors:
        follow = max(follow, f(nxt, order).deep)
    ans = Record(cur, follow + 1)
    order[cur] = ans
    return ans
